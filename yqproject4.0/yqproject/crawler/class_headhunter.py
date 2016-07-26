#coding=utf-8
__author__ = 'yc'

from class_save_data import *

class Headhunter(Database):
    def __init__(self):
        Database.__init__(self)

    def get_info(self, name):
        """
        用于显示核心人物个人信息
        :param name: 用户名
        :return:{'user_id':'000','user_name':name,'fans_num':232,'follow_num':678885}
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT user_id, user_name, fans_num, follow_num FROM headhunter WHERE user_name = '%s'" % name
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) != 0:
                return rows[0]
            else:
                rows={'user_id':'000','user_name':name,'fans_num':232,'follow_num':678885}
                return rows