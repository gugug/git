
__author__ = 'yc'

from django.conf.urls import include, url
from yuqing.views import *


urlpatterns=[
    url(r'^ajax_list/$', ajax_list, name='ajax-list'),
    url(r'^ajax_dict/$', ajax_dict, name='ajax-dict'),
    url(r'^index/$',homepage,name='index'),
    url(r'^network/(?P<event_id>[^/]+)/(?P<ctime>[^/]+)/$',network,name='network'),
    url(r'^linechart/(?P<topic>[^/]+)/$',line_chart,name='linechart'),

]