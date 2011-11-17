from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login as userlogin, logout as userlogout
from django.forms.util import ErrorList
from django.shortcuts import render_to_response

from models import *
from forms import *
from apps.geo.models import *
from apps.core.models import *
from apps.spiffs.models import *

import datetime
import simplejson as json

from libs.utils import Response
import settings

def invitation_landing(request,invid,name):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/members/')
		
	first_name = ""
	last_name = ""
	
	parts = name.split("/")
	if len(parts) == 1:
		first_name = parts[0]
	elif len(parts) > 1:
		first_name = parts[0]
		last_name = parts[1]
	try:	
		i = Invitation.objects.get(curl=invid)
	except:
		raise Http404()
	
	if i.prospect.first_name == first_name and i.prospect.last_name == last_name and (i.status == 'SENT' or i.status == 'VISITED'):
		form = SignupForm(
							{
								"email" 		: i.prospect.email,
								"first_name" 	: i.prospect.first_name,
								"last_name" 	: i.prospect.last_name,
							}
						)
		
		request.session["invitation"] = i.id
		
		i.status = 'VISITED'
		i.save()
		
		return Response.render_form(request,'members/signup.html',form,errors=False)
	else:
		raise Http404()
	
	#p  = Prospect.objects.get(id=invid,first_name=first_name,last_name=last_name,source="Invitation")
	
	return HttpResponse(i)


def fbinvite(request):
	params = {"appId" : settings.CRED["FACEBOOK_APP_ID"] }
	return render_to_response("members/fbinvite.html",params)
	
def invite(request):
	if not request.user.is_authenticated():
		return Response.send_to_login(request)
	
	message = None
	
	if request.method == 'POST': 
		form = InvitationForm(request.POST)
		if form.is_valid():	
			
			
			p = Prospect(
							email = form.cleaned_data['email'],
							first_name	= form.cleaned_data['first_name'],
							last_name = form.cleaned_data['last_name'],
							source	= "Invitation"
							)
			p.save()
			
			
			
			invitation = Invitation(			
						sender 		= User.instance(request.user),
						prospect 	= p
					)
			invitation.create_curl()
			invitation.save()
			invitation.sendmail()
		
			message = "An invitation has been sent to %s " % (p.email)
			form = InvitationForm()	
		else:
			pass
	else:
		form = InvitationForm()
	
	return Response.render ("members/invite.html",{"form" : form , "appId" : settings.CRED["FACEBOOK_APP_ID"], "message" : message},request)

def profile(request):
	if not request.user.is_authenticated():
		return Response.send_to_login(request)
	
	param = {}
	try:
		param['needs_username_correction'] = request.session['needs_username_correction']
	except Exception,ex:
		param['needs_username_correction'] = False
		
	user = User.instance(request.user)
	if request.method == 'POST': 
		form = ProfileForm(request.POST)
		param['form'] = form
		param['errors'] = True	
		
		if form.is_valid():	
			username 		= form.cleaned_data['username']
			try:
				u = User.objects.get(username=username)
				if u.id != user.id:
					form.errors['username']  	= ErrorList( [u'Username already exists'])
			except:
				pass
			
			email			= form.cleaned_data['email']
			try:
				u = User.objects.get(email=email)
				if u.id != user.id:
					form.errors['email']  		= ErrorList([u'Username with this email already exists'])
			except:
				pass
			
			if not form.errors:
				user.username		= username
				user.email			= email
				
				user.first_name		= form.cleaned_data['first_name']
				user.last_name		= form.cleaned_data['last_name']
			
				user.gender	 		= form.cleaned_data['gender']
				user.dob 			= form.cleaned_data['dob']
	
				user.address.zipcode 		= form.cleaned_data['zipcode']
				user.address.street_line_1	= form.cleaned_data['street_line_1']
				user.address.street_line_2	= form.cleaned_data['street_line_2']
				user.address.city			= form.cleaned_data['city']
				user.address.state			= form.cleaned_data['state']
				user.address.country		= Country.objects.get(id=form.cleaned_data['country'])
				
				user.address.save()
				user.save()
				
				try:
					del request.session['needs_username_correction']
				except:
					pass
				
				return HttpResponseRedirect('/members/')
			else:
				pass
		
			
	else:
		
		
		fn = user.first_name
		if fn[0] == "(" and fn[-1] == ")":
			fn = fn[2:-3]
		
		ln = user.last_name
		if ln[0] == "(" and ln[-1] == ")":
			ln = ln[2:-3]
		
		em = user.email
		if em is None or em == "" or em == "None":
			em = ""
		
		un = user.username
		
		if param['needs_username_correction']:
			un = ""
			
		param['form'] = ProfileForm(
							{
								"username" 		: un,
								"email" 		: em,
								"first_name" 	: fn,
								"last_name" 	: ln,
								"gender" 		: user.gender,
								"dob" 			: user.dob,
								"zipcode" 		: user.address.zipcode,
								"street_line_1" : user.address.street_line_1,
								"street_line_2" : user.address.street_line_2,
								"city" 			: user.address.city,
								"state" 		: user.address.state,
								"country" 		: user.address.country.id,
							}
						)
		param['errors'] = False		
	return Response.render ('members/profile.html',param,request)
	

def signup (request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/members/')
			
	if request.method == 'POST': 
		form = SignupForm(request.POST)
		
		
		if form.is_valid():
			email1		= form.cleaned_data['email']
			email2		= form.cleaned_data['email2']
		
			if email1 != email2:
				form.errors['email2'] 	= ErrorList([u'Emails do not match'])
			
			try:
				User.objects.get(email=email1)
				form.errors['email']  		= ErrorList([u'Username with this email already exists'])
			except:
				pass
					
			username 		= form.cleaned_data['username']
			try:
				User.objects.get(username=username)
				form.errors['username']  	= ErrorList([u'Username already exists'])
			except:
				pass
			
			password			= form.cleaned_data['password']
			
			
			if not form.errors:
				first_name		= form.cleaned_data['first_name']
				last_name		= form.cleaned_data['last_name']
			
				gender	 		= form.cleaned_data['gender']
				dob 			= form.cleaned_data['dob']
	
				
			
				country = Country.objects.get(id=1)
				
				phonenumber = PhoneNumber(
					countrycode = 0,
					carriercode = 0,
					number 		= 0,
				)
				phonenumber.save()
				
				address = Address(
					zipcode 		= "",
					street_line_1	= "",
					street_line_2	= "",
					city			= "",
					state			= "",
					country			= country,
					location 		= country.location,
					phonenumebr		= phonenumber
				)
			
				address.save()
			
				user = User (
					username		= username,
					email			= email1,
					password		= User.encode_pass(password),
					first_name		= first_name,
					last_name		= last_name,
					dob				= dob,
					gender			= gender,
					address			= address,
					verification	= User.create_verification("1"),
					points 			= 0,
				)
				user.save()
				
				
				reffered_by = False
				try:
					ref_id = request.session["f"]
					reffered_by = User.objects.get(id=ref_id)
					del request.session["f"]
				except:
					pass
		
		
				invitation = False
				try:
					invitation = Invitation.objects.get(id=request.session["invitation"])
					del request.session["invitation"]
				except:
					try:
						invitation = Invitation.objects.get(prospect=Prospect.objects.get(email=user.email))
					except:
						pass
							
				if invitation:
					reffered_by = invitation.sender
					invitation.status = "SIGNUP"
					invitation.save()
					
				if reffered_by:
					ref = Referral(reffered_by=reffered_by,reffered_to=user)
					ref.save()
				
				user.send_verification_mail()
				return HttpResponseRedirect('/members/')
				
	else:
		try:
			request.session["f"] = request.GET["f"]
			return HttpResponseRedirect("/members/signup/")
		except:
			pass
			
		form = SignupForm()
	
	return Response.render_form (request,'members/signup.html',form)
	

def dashboard(request):
	if request.user.is_authenticated():
		params = {}
		
		params["user"] = User.instance(request.user)
	
		#1- activities chart
		params["activities"]	=	Activity.chart(params["user"],5)
		
		#2- my deals [deals he is interested in]
		params["mydeals"] =	UserDeal.objects.filter(user=params["user"]).extra(order_by=['-added'])[:5]
		
		#3- friends
		params["friends"] = params["user"].friends
		
		#4- recent activities
		params["recent_points"] = Activity.recent(params["user"],5)
		
		
		#-5 rewards
		
		
		#-6 invite
		params["iform"] = InvitationForm()
		
		
		
		
		
		return Response.render("members/dashboard.html",params,request)
	else:
		return Response.send_to_login(request)


def index (request):
	pass
		
def logout (request):
	if request.user.is_authenticated():
		userlogout(request)
		
	return HttpResponseRedirect('/members/login/')

def login (request):	
	if request.user.is_authenticated():
		return HttpResponseRedirect('/members/')
	
	if request.method == 'POST': 
		form = LoginForm(request.POST)
		if form.is_valid():
			username 				= form.cleaned_data['username']
			password				= form.cleaned_data['password']
			
			user = authenticate(username=username, password=password)
			
			if user is None:
				form.errors["username"]	= ErrorList([u'Invalid Username or Password'])
			else:
				s_user = User.objects.get(id=user.id)
				if s_user.verification.verified == False:
					form.errors["username"]	= ErrorList([u'User must be verified first due to "%s"' % (s_user.verification.purpose)])
				elif user.is_active:
					userlogin(request,user)
					return Response.send_to_destination(request)
				else:
					form.errors["username"]	= ErrorList([u'Account Disabled'])
	else:
		form = LoginForm()
		
	return Response.render_form (request,'members/login.html',form)



def settings_view(request):
	if request.user.is_authenticated():
		if request.method == 'POST': 
			for cid in request.POST: 
				try:
					c = Config.objects.get(id=cid)
					c.value = request.POST[cid]
					c.save()
				except:
					pass
		
		configList = User.instance(request.user).get_all_config()
		
		clm 		= 1
		total_clm	= 2
		
		table = []
		row   = {}
		
		for title in configList:
			row[title] = configList[title]
			clm = clm + 1
			if clm > total_clm:
				table.append(row)
				row = {}
		
		table.append(row)
		
		c = {"table":table}
		
		c.update(csrf(request))	
		return Response.render("members/settings.html", c , request)
	else:
		return Response.send_to_login(request)
	
def verify(request,code):
	#http://localhost/members/v/yxdRRWPx22Fr/
	if request.user.is_authenticated():
		return HttpResponseRedirect('/members/')
		
	try:
		user = User.objects.get(verification=Verification.objects.get(code=code))
		if user.verification.purpose == "1" and user.verification.verified == False:
			user.verification.verified 		= True
			user.verification.verified_on 	= datetime.datetime.now()
			user.verification.save()
			
			user.is_active 					= True	
			user.is_staff					= True
			user.save()
			
			try:
				ref = Referral.objects.get(reffered_to=user)
				inv = Invitation.objects.get(sender=ref.reffered_by)
				inv.status = 'VERIFIED'
				inv.save()
			except:
				pass
			
		return Response.send_to_login(request,False)
	
	except Exception,e:
		return HttpResponse(e)


def like_deal(request,deal_id):
	if request.user.is_authenticated():
		user = User.instance(request.user)
		try:
			deal = Deal.objects.get(id=deal_id)
		except Deal.DoesNotExist, dne:
			return Response({"success":False,"message":"Deal does not exist"})
		try:
			ud = UserDeal.objects.get(deal=deal,user=user)
			return Response.json({"success":False,"message":"Already in my deals","at":str(ud.added)})
		except UserDeal.DoesNotExist,ex:
			ud = UserDeal(deal=deal,user=user)
			ud.save()
			return Response.json({"success":True,"message":"success added to my deals", "id":ud.id})
	else:
		return Response.send_to_login(request)


def landed(request):
	try:
		response = HttpResponse("SUCCESS")
		max_age = 365*24*60*60
		expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
		response.set_cookie("location", request.GET["loc"], max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN)
		response.set_cookie("email", request.GET["email"], max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN)
		
		return response
		
	except Exception, ex:
		return HttpResponse("FAILURE" + str(ex.message))
		
## TEST CODE
## TODO TO BE REMOVED FROM PRODUCTION

def clear_loc(request):
	response = HttpResponseRedirect("/members/")
	
	max_age = 0
	expires = datetime.datetime.strftime(datetime.datetime.utcnow(),"%a, %d-%b-%Y %H:%M:%S GMT")
	
	response.set_cookie("location", "", max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN)
	response.set_cookie("email",    "", max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN)

	return response
	
def test (request):	
	return HttpResponse(request.COOKIES["location"])

def allow_me (request):
	from apps.security.models import AllowedHosts
	try:
		AllowedHosts.objects.get(ip=request.META["REMOTE_ADDR"])
	except AllowedHosts.DoesNotExist, dne:	
		AllowedHosts(ip=request.META["REMOTE_ADDR"]).save()
	return Response.send_to("/")
