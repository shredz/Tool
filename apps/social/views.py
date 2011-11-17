from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login as userlogin , get_backends 

from apps.social.facebook import Facebook 
from apps.social.twitter import Twitter 
import settings

from apps.geo.models import *
from apps.core.models import *
from apps.members.models import *
from apps.social.models import *
from apps.spiffs.models import *

from libs.utils import ValueManager,Response
from oauth import oauth
import oauth2


import simplejson as json
import datetime,urllib


def share_deal(request,deal_id):
	if not request.user.is_authenticated():
		return Response.send_to_login(request)
	
	user = User.instance(request.user)
	facebook = Account.get_for_user(user,"facebook")
	
	if not facebook:
		return HttpResponse("Not connected TO facebook YET")
		
	
	try:
		deal = Deal.objects.get(id=deal_id)		
		deal = Deal.assign_left([deal])[0]
		deal.link = "http://ldev.spiffcity.com/spiffs/deal/"+str(deal.id)+"/"
		
		##TODO create activity to get points
		
		deal.shared(user)
		
		##
		
		return Response.render("spiffs/fbshare.html",{"deal":deal,"fb_api_key":settings.CRED['FACEBOOK_APP_ID'],"access_token":facebook.oauth_token},request)
		
		#fb = Facebook(settings.CRED['FACEBOOK_APP_ID'] ,settings.CRED['FACEBOOK_APP_SECRET'],settings.CRED['FACEBOOK_RETURN_URL'])
		#data = fb.share_deal(facebook, deal)
		#Response.html(data)
		#return Response.render("spiffs/deal.html",{"deal":deal},request)
		
	except Deal.DoesNotExist, dne :
		Response.not_found()
		
		
def feed_account (request,network):
	if not request.user.is_authenticated():
		return {"Error":"Not logged in"}
	try:
		user = User.instance(request.user)
	except User.DoesNotExist, dne:
		return {"Error":"Not Allowed"}
	
	account = Account.get_for_user(user,network)
	if account is None:
		return {"Error":"Not connected to %s" % (network)}
	else:
		return account

def facebook_feed(request):
	f_acc = feed_account(request,"facebook")
	if f_acc is dict:
		return Response.json(f_acc)
	
	fb = Facebook(settings.CRED['FACEBOOK_APP_ID'] ,settings.CRED['FACEBOOK_APP_SECRET'],settings.CRED['FACEBOOK_RETURN_URL'])
	params = {"feed" : fb.news_feed(f_acc.oauth_token)}
	return Response.render_html("social/facebook_feed.html",params)
	
	
def twitter_feed(request):
	f_acc = feed_account(request,"twitter")
	if f_acc is dict:
		return Response.json(f_acc)
	
	twt = Twitter(settings.CRED['TWITTER_CONSUMER_KEY'] ,settings.CRED['TWITTER_CONSUMER_SECRET'],settings.CRED['TWITTER_RETURN_URL'])
	
	#return Response.json(twt.home_timeline(f_acc))
	
	params = {"feed":twt.home_timeline(f_acc)}
	return Response.render_html("social/twitter_feed.html",params)
			


def index(request):
	if not request.user.is_authenticated():
		return Response.send_to_login(request)
	
	user = User.instance(request.user)
	params = {"errors":[]}
	
	params["facebook"] = Account.get_for_user(user,"facebook")
	params["twitter"] = Account.get_for_user(user,"twitter")
		
	return Response.render("social/social.html",params,request)

def connect_to_facebook(request):
	fb = Facebook(settings.CRED['FACEBOOK_APP_ID'] ,settings.CRED['FACEBOOK_APP_SECRET'],settings.CRED['FACEBOOK_RETURN_URL'])
	
	try:
		code = request.GET['code']
	except:
		return fb.connect_to_facebook(request)
		
	request.session['token'] = code
	return after_connect(request,fb.authenticate_facebook(request,code),"facebook")
		

def connect_to_twitter(request):
	twt= Twitter(settings.CRED['TWITTER_CONSUMER_KEY'] ,settings.CRED['TWITTER_CONSUMER_SECRET'],settings.CRED['TWITTER_RETURN_URL'])
	
	try:
		verifier = request.GET['oauth_verifier']		
	except:
		return twt.connect_to_twitter(request)
	
	denied = request.GET.get('denied', None)
	if denied is None:		
		try:
			request_token = request.session['request_token']
		except:
			return twt.connect_to_twitter(request)
		
		token = oauth.OAuthToken.from_string(request_token)
		
		if token.key != request.GET.get('oauth_token', 'no-token'):
			del request.session ['request_token']
			return twt.connect_to_twitter(request)
		
		try:
			access_token = twt.get_access_token(token,verifier)
		except KeyError , e:
			return twt.connect_to_twitter(request)
			
		request.session['access_token'] = access_token
		twt_user = twt.authenticate_twitter(access_token)
		twt_user['access_token'] = access_token
		
		return after_connect(request,twt_user,"twitter")				
	else:
		#message
		return HttpResponseRedirect("/members/")

def get_field(net_user,field,network):
	if network == "facebook":
		if field == "location":
			return net_user["location"]["name"]
		elif field == "username":
			return net_user["username"]
		elif field == "email":
			return net_user["email"]
		elif field == "first_name":
			return net_user["first_name"]
		elif field == "last_name":
			return net_user["last_name"]
		elif field == "gender":
			return net_user["gender"]
			
	elif network == "twitter":
		if field == "location":
			return net_user["location"]
		elif field == "username":
			return net_user["screen_name"]
		elif field == "email":
			return "None"
		elif field == "first_name":
			return net_user["name"]
		elif field == "last_name":
			return ""
		elif field == "gender":
			return ""
			
	return net_user[field]
			
def after_connect(request , net_user , network):
	try:
		account = Account.objects.get(uid=net_user['id'])
		
		###
		if request.user.is_authenticated():
			if account.spiffuser.id != request.user.id:
				account.spiffuser = User.instance(request.user)
				
				
				## WARN TO GO WITH THAT ACCOUNT INSTEAD		
		###
		
		backend = get_backends()[0]
		account.spiffuser.backend = "%s.%s" % (backend.__module__, backend.__class__.__name__)
		userlogin(request,account.spiffuser)
		
		if network == "facebook":
			account.oauth_token = net_user['access_token']
		elif network == "twitter":
			account.oauth_token = net_user['access_token'].key
			account.oauth_token_secret = net_user['access_token'].secret
		account.save()
		
	except Account.DoesNotExist:
		needs_username_correction = False
		
		if request.user.is_authenticated():
			user = User.instance(request.user)
		else:
			country = Country.objects.get(id=1)
				
			phonenumber = PhoneNumber(
				countrycode = 0,
				carriercode = 0,
				number 		= 0,
			)
			phonenumber.save()
				
			address = Address(
				zipcode 		= '',
				street_line_1	= '',	
				street_line_2	= '',
				city			= '',
				state			= '',
				country			= country,
				location 		= country.location,
				phonenumebr		= phonenumber
			)
			
			try:
				loc = get_field(net_user,"location",network)
				address.street_line_1	= loc
				address.city			= loc
			except:
				pass
				
			address.save()
			
			username = get_field(net_user,"username",network)
			
			
			try:
				User.objects.get(username=username)
				username = get_field(net_user,"id",network)
				needs_username_correction = True
				request.session['needs_username_correction'] = True
			except:
				pass
			
			user = User (
				username		= username,
				email			= get_field(net_user,"email",network),
				password		= "0000",
				first_name		= '',
				last_name		= '',
				dob				= datetime.datetime.now(),
				gender			= '',
				address			= address,
				verification	= User.create_verification("1",True),
				is_active		= True,
				is_staff		= True,
				points			= 0,
			)
			
			try:
				user.first_name		= get_field(net_user,'first_name',network),
				user.last_name		= get_field(net_user,'last_name',network),
				user.gender			= ValueManager.translate_gender(get_field(net_user,'gender',network))
			except:
				pass
			
			user.save()
			
			backend = get_backends()[0]
			user.backend = "%s.%s" % (backend.__module__, backend.__class__.__name__)
			userlogin(request,user)
		
		token = net_user['access_token']
		del net_user['access_token']
		
		account = Account(
			uid					= get_field(net_user,'id',network),
			oauth_token			= "",
			oauth_token_secret	= "",
			other_data			= json.dumps(net_user),
			spiffuser			= user,
			account_type		= network
		)
		account.save()
		
		if network == "facebook":
			account.oauth_token 		= token
		elif network == "twitter":
			account.oauth_token 		= token.key
			account.oauth_token_secret 	= token.secret
			
		if needs_username_correction:
			return HttpResponseRedirect("/members/profile/")		
			
	return HttpResponseRedirect("/")
	
	


