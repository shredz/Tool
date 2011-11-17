from libtwt import oauthtwitter2 as oauthtwitter
import oauth2
import settings
import urllib
import simplejson as json

from django.http import HttpResponseRedirect , HttpResponse

		#https://api.twitter.com/1/direct_messages.json
		#https://api.twitter.com/1/statuses/home_timeline.json
		#https://api.twitter.com/1/statuses/mentions.json
		#https://api.twitter.com/1/statuses/user_timeline.json screen_name=any
		#https://api.twitter.com/1/favorites.json


class Twitter:
	def __init__(self,twt_app_key, twt_app_secret, return_url):
		self.twt_app_key = twt_app_key
		self.twt_app_secret = twt_app_secret
		self.return_url = return_url
		
	def connect_to_twitter(self,request):
	
		twt = oauthtwitter.TwitterOAuthClient(self.twt_app_key, self.twt_app_secret)
		request_token = twt.fetch_request_token(callback = self.return_url)    
		request.session['request_token'] = request_token.to_string()	
		return HttpResponseRedirect(twt.authorize_token_url(request_token))
	
	def authenticate_twitter(self,twitter_access_token):
		twitter = oauthtwitter.TwitterOAuthClient(self.twt_app_key, self.twt_app_secret)
		tw_profile = twitter.get_user_info(twitter_access_token)  
		return tw_profile 
		
	def get_access_token(self,token, verifier):
		twt = oauthtwitter.TwitterOAuthClient(self.twt_app_key, self.twt_app_secret)
		return twt.fetch_access_token(token, verifier)
	
	def home_timeline(self,twitter):
		token = oauth2.Token(twitter.oauth_token,twitter.oauth_token_secret)
		consumer = oauth2.Consumer(settings.CRED['TWITTER_CONSUMER_KEY'] ,settings.CRED['TWITTER_CONSUMER_SECRET'])
		client = oauth2.Client(consumer,token)
		data = {'count':200}
		request_uri = 'https://api.twitter.com/1/statuses/home_timeline.json'
		resp, content = client.request(request_uri, 'GET', urllib.urlencode(data))
		return json.loads(content)
