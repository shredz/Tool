from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', 		include('django.contrib.admindocs.urls')),
    (r'^admin/', 			include(admin.site.urls)),
    (r'^members/', 			include("apps.members.urls")),
	(r'^importer/', 		include("apps.importer.urls")),
	(r'^reporting/', 		include("apps.reporting.urls")),
	(r'^social/', 			include("apps.social.urls")),
	(r'^spiffs/', 			include("apps.spiffs.urls")),
	
	(r'^(?P<p>(.*))/$', 	"views.page"),
	(r'^$', 				"views.index"),
)
