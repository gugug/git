
__author__ = 'yc'

from django.conf.urls import include, url
from yuqing.views import *


urlpatterns=[
    url(r'^ajax_list/$', ajax_list, name='ajax-list'),
    url(r'^ajax_dict/$', ajax_dict, name='ajax-dict'),
    url(r'^index/$',homepage,name='index'),
    url(r'^network/',network,name='network'),
    url(r'^linechart/$',line_chart,name='linechart'),

]