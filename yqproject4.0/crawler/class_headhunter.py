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
            sql = "SELECT DISTINCT user_name, fans_num, follow_num, profile FROM headhunter WHERE user_name = '%s'" % name
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) != 0:
                fans_num = rows[0]['fans_num']
                follow_num = rows[0]['follow_num']
                profile = rows[0]['profile']
                info = "粉丝数:"+str(fans_num)+",关注数:"+str(follow_num)+'   简介:'+str(profile)
                return info
            else:
                info = "粉丝数:23879,关注数:23"
                return info