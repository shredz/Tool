from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect, Http404


from apps.spiffs.models import *
from apps.members.models import *

from libs.utils import Response

def index(request):
	return Response.render("general/main.html" , {},request)

def page(request,p):	
	if p == 'how-it-works':
		return howitworks(request)
	elif p == 'about-us':
		return about(request)	
	elif p == 'merchants':
		return merchants(request)	
	elif p == 'groupon':
		return groupon(request)	
	else:		
		raise Http404()
	
def howitworks(request):
	return Response.render("general/howitworks.html",{},request)

def about(request):
	return Response.render("general/aboutus.html",{},request)

def merchants(request):
	return Response.render("general/merchants.html",{},request)

def groupon(request):
	return Response.render("general/groupon.html",{},request)
