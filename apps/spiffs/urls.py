from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^index/', 							"apps.spiffs.views.index"),
    (r'^search/$', 							"apps.spiffs.views.search"),
    
    (r'^deals/new/(?P<page>([0-9]*))/$', 			"apps.spiffs.views.new_deals"),
    (r'^deals/gmap/(?P<page>([0-9]*))/$', 			"apps.spiffs.views.gmap"),
    (r'^deals/sdeal/(?P<page>([0-9]*))/$', 			"apps.spiffs.views.show_deal"),
    (r'^deallist/(?P<cat_id>([0-9]*))/$', 			"apps.spiffs.views.deallist"),
    
    (r'^deals/approve/(?P<deal_id>([0-9]*))/$',	"apps.spiffs.views.approve_deal"),
    (r'^deals/reject/(?P<deal_id>([0-9]*))/$',  "apps.spiffs.views.reject_deal"),
    
    (r'^deals/(?P<page>([0-9]*))/$', 			"apps.spiffs.views.deals"),
    (r'^deal/(?P<deal_type>([a-zA-Z]*))/(?P<deal_id>([0-9]*))/$',"apps.spiffs.views.deal"),
    
    (r'^v/(?P<deal_type>([a-zA-Z]*))/(?P<deal_id>([0-9]*))/$',"apps.spiffs.views.visited"),
    (r'^deals/map/$', 			"apps.spiffs.views.map"),
    (r'^deals/list/$', 			                        "apps.spiffs.views.list"),
    (r'^deals/ajax_search/(?P<keyword>([a-zA-Z]*))/$', 			"apps.spiffs.views.ajax_search"),
    (r'^deals/ajax_list_deal/(?P<city_id>([a-zA-Z]*))/$', 			"apps.spiffs.views.ajax_list_deal"),
    
    
)
