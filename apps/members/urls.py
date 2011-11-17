from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^signup/$', 					"apps.members.views.signup"),
    (r'^login/$' ,  				"apps.members.views.login"),
    (r'^logout/$' ,  				"apps.members.views.logout"),
    (r'^invite/$',					"apps.members.views.invite"),
    (r'^fbinvite/$',				"apps.members.views.fbinvite"),
    
    (r'^settings/$', 				"apps.members.views.settings_view"),
    (r'^profile/$', 				"apps.members.views.profile"),
    (r'^v/(?P<code>(.*))/$', 		"apps.members.views.verify"),
    
    (r'^i/(?P<invid>([0-9a-zA-Z]*))/$', "apps.members.views.invitation_landing",{"name":"/"}),
    (r'^i/(?P<invid>([0-9a-zA-Z]*))/(?P<name>(.*))/$', "apps.members.views.invitation_landing"),
    
    (r'^like/(?P<deal_id>([0-9]*))/$', "apps.members.views.like_deal"),
    
    (r'^landed/$', "apps.members.views.landed"),
    
    #TODO NEXT LINES EXCEPT LAST ARE TEST AND ARE TO BE REMOVED FROM PRODUCTION
    (r'^test/$', "apps.members.views.test"),
    (r'^clc/$', "apps.members.views.clear_loc"),
    
    (r'^ALLOW_ME_TO_GET_THERE/$', "apps.members.views.allow_me"),
    
    (r'^$', "apps.members.views.dashboard"),
)
