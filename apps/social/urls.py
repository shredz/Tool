from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 				"apps.social.views.index"),
    
    (r'^facebook/connect/$', 	"apps.social.views.connect_to_facebook"),
	(r'^facebook/feed/$', 	"apps.social.views.facebook_feed"),
    
    (r'^twitter/connect/$', 	"apps.social.views.connect_to_twitter"),
    (r'^twitter/home_timeline/$', 	"apps.social.views.twitter_feed"),
    
    (r'^share/deal/(?P<deal_id>([0-9]*))/$', 	"apps.social.views.share_deal"),
)
