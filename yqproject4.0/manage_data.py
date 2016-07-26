#coding=utf-8

import os
from crawler.class_save_data import *

db = Database()
exist_topic_list = []
for root, dir, file in os.walk('documents/topic',False):
    if len(dir) != 0 and len(file) == 0:
        # print 'root',root
        tmp = root.split('/')
        if len(tmp) == 3:
            title = tmp[2]
            exist_topic_list.append(title)

for i in exist_topic_list:
    with db.conn:
        cur = db.conn.cursor(MySQLdb.cursors.DictCursor)
        # sql = "select * from event EXCEPT (select event_id from event where etopic = %s)" % i
        print sql
        cur.execute(sql)




