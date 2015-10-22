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

from class_all_id import Sina
import multiprocessing as mul


if __name__ =='__main__':
    crawler = Sina()
    uid=crawler.getUser(1,2,1,2)
    pool=mul.Pool(processes=5)
    for i in uid:
        run=[crawler.getFans(i,1,2),crawler.getFollow(i,1,2),crawler.getPage(i,1,2)]
        for func in run:
            pool.apply_async(func)
    pool.close()
    pool.join()
