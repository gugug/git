#coding=utf-8
__author__ = 'yc'
from django.contrib import admin
from django.conf.urls import url,patterns
from dua.views import *
from django.views.generic.list import ListView
from dua.models import *

urlpatterns = [
    url(r'^login',login_page,name='login_page'),
    url(r'^database/(?P<id>[0-9]+)',show_database,name='show_db'),
    url(r'^index',index,name='index'),
    url(r'^register',register_page,name='register_page'),
    url(r'^logout',logout_page,name='logout_page'),
    url(r'^main_page',main_page,name='main_page'),
    url(r'^get_id',get_id,name='get_id'),
]
