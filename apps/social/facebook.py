from django.http import HttpResponseRedirect, HttpResponse
from libs.utils import Exporter
import settings

import urllib, simplejson as json, cgi
import urllib2

class Facebook(Exporter):
	
	def __init__(self, fb_app_id,fb__app_secret,return_url):
		Exporter.__init__(self)

		self.fb_app_id = fb_app_id
		self.fb__app_secret =fb__app_secret
		self.return_url = return_url
	
	def connect_to_facebook(self,request):
		args = {
			'client_id': self.fb_app_id,
			'redirect_uri': self.return_url,
			'scope': 'email,publish_stream,user_birthday,friends_birthday,user_events,user_status,read_stream,offline_access',
		}
		return HttpResponseRedirect('https://www.facebook.com/dialog/oauth?' + urllib.urlencode(args))
	
	def get_access_token(self,token):
		args = {
			'client_id': self.fb_app_id,
			'client_secret': self.fb__app_secret,
			'redirect_uri': self.return_url,
			'code': token,
		}

		target = urllib.urlopen('https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(args)).read()
		response = cgi.parse_qs(target)
		return response['access_token'][-1]
	
	
	def share_deal(self,account,deal):
	
		params = {
			"picture" 	: deal.image_url,
			"link"		: "http://ldev.spiffcity.com/social/deal/"+str(deal.id),
			"name"		: deal.title,
			"description":deal.description,
			"access_token":account.oauth_token
		}
		
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
		urllib2.install_opener(opener)
		
		f = opener.open('https://graph.facebook.com/'+str(account.uid)+'/feed/', params)
		data = f.read()
		f.close()
		
		return data
		
		
				#message, picture, link, name, caption, description, source
	
	
	def news_feed(self,access_token):
		feeds = json.loads(urllib.urlopen('https://graph.facebook.com/me/home?' + urllib.urlencode(dict(access_token=access_token))).read())
		return feeds
	
	def authenticate_facebook (self,request , token):
		access_token = self.get_access_token(token)
		fb_profile = json.loads(urllib.urlopen('https://graph.facebook.com/me?' + urllib.urlencode(dict(access_token=access_token))).read())
		request.session['access_token'] = access_token
		fb_profile['access_token'] = access_token

		return fb_profile
        
