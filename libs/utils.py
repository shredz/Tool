class Importer:	
	def __init__(self,api_url):
		self.api_url = api_url
		
	def import_spiff_objects(self):
		return None


class Exporter:
	def __init__(self):
		pass
		
	def export_spiff_reports(self,objects):
		return None

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from apps.members.models import User
from apps.members.forms import SignupForm,LoginForm
from apps.social.models import Account
from django.core.context_processors import csrf

import simplejson as json
import settings, datetime, time

from apps.geo.ipinfo import getcity

class Message:
	def __init__ (msg,mtype="information"):
		self.msg = msg
		self.type = mtype
	
	@staticmethod
	def set_message(request,msg):
		try:
			if request.session["messages"] is not list:
				request.session["messages"] = []
		except:
			request.session["messages"] = []
		request.session["messages"].append(msg)






class ValueManager:
	@staticmethod
	def format_date(data , f1 , f2, cut_after = None):
		if cut_after:
			data = data.rsplit(cut_after,1)[0]
		return time.strftime (f2,time.strptime(data,f1))

	@staticmethod
	def translate_bytes(s):
		news = ''
		for i in range(len(s)):
			num = ord(s[i])
			if num > 127:
				c = '&#0'+str(num)+';'
			else:
				c = s[i]
			news += c
		return news
					
				
	@staticmethod 
	def translate_gender(gender):
		gender = gender.lower()
		
		if gender == "f" or gender == "female" or  gender == "fm" or gender == "she" or gender == "her":
			return "F"
		elif gender == "m" or gender == "male" or  gender == "he" or gender == "his":
			return "M"
		else:
			return ""

class link:
	def __init__(self,cssclass, link):
		self.cssclass = cssclass
		self.link = link
	

class Response:

	@staticmethod
	def render_html(template,params):
		return render_to_response(template,params)
	
	@staticmethod
	def not_found():
		raise Http404()
	
	@staticmethod
	def json(data):
		return HttpResponse(json.dumps(data))
	
	@staticmethod
	def html(data):
		return HttpResponse(data)
	
	@staticmethod
	def send_to (dest):
		return HttpResponseRedirect(dest)
	
	@staticmethod
	def render (template,params,request):
		getloc = False
		
		if request.user.is_authenticated():
		
			try:		
				params['user'] 		= User.instance(request.user)
			except User.DoesNotExist, dne:
				return HttpResponseRedirect("/admin/")
			
			params['facebook']  = Account.get_for_user(params['user'],"facebook")
			params['twitter']  = Account.get_for_user(params['user'],"twitter")
			
			params["loc"]     = params['user'].address.city
			if params["loc"] == "":
				getloc = True
			
		else:
			params['signupform'] = SignupForm()
			params['loginform'] = LoginForm()
			getloc = True
		
		if getloc:
			try:
				params["loc"]   = request.COOKIES['location']
				email = request.COOKIES['email']
			except:
				params['city']	  = getcity(settings.CRED["IPINFO_API_KEY"],request.META["REMOTE_ADDR"])
				params['landing'] = True

		#TODO REMOVE THIS TEMP HACK
		
		#params['twitter'] = True
		#params['landing'] = True
		#### END HACKS

			
		params['days'] = range(1,32)
		params['years']= range(1950,2012)
		params["social_links"] 	= [
									link("a","#"),
									link("b","#"),
									link("c","#"),
									link("d","#"),
									link("ali","#"),
									link("pic","#")
								]
		
		params["media"] = settings.MEDIA_URL
		params.update(csrf(request))
		response = render_to_response(template,params)
		
		max_age = 365*24*60*60
		expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
		response.set_cookie("_l_m_n_", "_o_P_", max_age=max_age)
		return response
		
		
		

	@staticmethod
	def render_form(request,template,form,errors=True):
		c = {'form': form}
		c['errors'] =  errors
		c.update(csrf(request))	
		return Response.render(template, c , request)
	
	@staticmethod
	def send_to_login (request,save=True):
		if save:
			request.session['destination'] = request.META['QUERY_STRING']
		return HttpResponseRedirect('/members/login/')

	
	@staticmethod
	def send_to_destination(request,url='/'):
		try:
			dest = request.session['destination']
			if dest is not None:
				return HttpResponseRedirect(dest)
		except:
			pass
		return HttpResponseRedirect(url)
