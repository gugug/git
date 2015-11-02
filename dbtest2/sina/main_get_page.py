#coding=utf-8
__author__ = 'yc'

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","dbtest2.settings")
django.setup()

from class_mysql_uid import *
from class_page import *
a=Database()
django.setup()
b=Page()
a.get_mysql_user()
b.sleep()
c=b.download()
b.getPage(c,1,2)