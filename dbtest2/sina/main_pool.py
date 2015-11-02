#!/usr/bin/env python
#coding=utf-8
'''
9.3进程池
'''
from class_mysql_uid import *
__author__ = 'yc'
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","dbtest2.settings")
django.setup()

from class_page import *
import multiprocessing as mul,json


if __name__ =='__main__':
    db = Database()
    page_crawler = Page()
    uid = db.get_mysql_user(61,1000)
    pool = mul.Pool(processes=20)
    for i in uid:
        run = [page_crawler.getPage(uid,1,10)]
        for func in run:
            pool.apply_async(func)
    pool.close()
    pool.join()

