from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^approval_list/$', 			"apps.importer.views.approval_list"),
    (r'^approve/(?P<p>([0-9]*))/$', "apps.importer.views.approve"),
    (r'^import_deals/', 			"apps.importer.views.import_deals"),
    (r'^import_gp_deals/', 			"apps.importer.views.import_gp_deals"),
    (r'^$', 						"apps.importer.views.index"),    
)
