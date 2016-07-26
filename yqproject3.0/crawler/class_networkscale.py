#coding=utf-8
__author__ = 'yc'
from crawler.class_save_data import *
from yqproject.settings import *

class NetworkScale(Database):
    def __init__(self):
        Database.__init__(self)

    def get_path(self,eid):
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT label_dir FROM networkscale WHERE event_id = '%s' limit 1" % eid
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) != 0:
                return rows[0]['label_dir']
            else:
                default = BASE_DIR+'/network/result/new_label_link.xls'
                rows={'label_dir':''}
                return rows['label_dir']