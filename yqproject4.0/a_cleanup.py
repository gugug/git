__author__ = 'yc'

from crawler.class_save_data import *
import shutil

class Clean():
    def __init__(self):
        self.conn = MySQLdb.connect(
            host='127.0.0.1',  # 192.168.235.36 fig #192.168.1.41 me #192.168.1.40 jie
            port=3306,
            user='root',
            passwd='123456',
            db='yuqing',
            charset='utf8', )

    def clean(self):
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql1 = "DELETE FROM event"
            sql2 = "Delete from content"
            cur.execute(sql1)
            cur.execute(sql2)
        shutil.rmtree('../yqproject/documents/topic')
        shutil.rmtree('../yqproject/static/sna/topic')

Clean().clean()