from django.http import HttpResponseRedirect, HttpResponse

from apps.security.models import AllowedHosts

class DomainMiddleware:
	def process_request(self, request):
		
		if "ALLOW_ME_TO_GET_THERE" in request.path:
			return
		
		if request.path[0:6] != "/admin":			
			try:
				AllowedHosts.objects.get(ip=request.META["REMOTE_ADDR"])
			except Exception, e:
				return HttpResponse("You are not allowed to visit this page from %s "% (request.META["REMOTE_ADDR"]))
			
		
			
		
		if request.get_host() == 'localhost':
			url = "http://192.168.1.143"+request.path
			if request.META['QUERY_STRING'] is not None:
				url = url + "?"+ request.META['QUERY_STRING']
			return HttpResponseRedirect(url)		
