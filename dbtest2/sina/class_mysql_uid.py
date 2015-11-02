__author__ = 'gu'
# -*- coding: UTF-8 -*-
# 来源：疯狂的蚂蚁的博客www.server110.com总结整理
import MySQLdb
import urllib, urllib2
import json
import simplejson
from class_all_id import *

class Database:
    def __init__(self):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/35'}

        self.conn= MySQLdb.connect(
            host='192.168.1.57',
            port = 3306,
            user='yc',
            passwd='uliuli520',
            db ='sina',
            charset='utf8',)
        self.user_list = []

    def get_mysql_user(self,begin,end):

        with self.conn:
            # 获取连接上的字典cursor，注意获取的方法，
            # 每一个cursor其实都是cursor的子类
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            # 执行语句不变
            cur.execute("SELECT * FROM sinauser WHERE ID >= "+str(begin) +" AND ID <= "+str(end) )
            # 获取数据方法不变
            rows = cur.fetchall()
            # 遍历数据也不变（比上一个更直接一点）
            dict_uid = dict()
            # print rows
            for row in rows:
                # 这里，可以使用键值对的方法，由键名字来获取数据
                # print "%s %s" % (row["user_id"], row["user_name"])
                # print "%s" % (row["user_id"])
                self.user_list.append(row["user_id"])
            # print user_list
            # dict_uid[row["user_id"]]=row["user_name"]
            return self.user_list


