#!/usr/bin/env python
#coding=utf-8
'''
9.3进程池
'''

__author__ = 'yc'
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","dbtest2.settings")
django.setup()

from test_page import *
from class_mysql_uid import *
import multiprocessing as mul,json
from class_login import *
from ProxyIP.proxyIp import *
if __name__ =='__main__':
    # ip=Login()
    # ip.changeIp()
    
    getProxyIpControl()
    setIpProxy(getIpInFile())

    db=Database()
    page_crawler =Page()
    uid=db.get_mysql_user(10,20)
    pool=mul.Pool(processes=5)
    for i in uid:
        run=[page_crawler.count(uid,i),page_crawler.getPage(i,1,2)]
        for func in run:
            pool.apply_async(func)
    pool.close()
    pool.join()
