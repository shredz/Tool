from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^index/',"apps.point.views.index"),
)