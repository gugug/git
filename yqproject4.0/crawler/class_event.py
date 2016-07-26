#coding=utf-8
__author__ = 'yc'

from class_save_data import *


class Event(Database):
    def __init__(self):
        Database.__init__(self)

    # def save_event_id(self,eid):
    #     with self.conn:
    #         cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
    #         sql = "Replace INTO event(event_id) VALUES ('%s')" % eid
    #         cur.execute(sql)
    #         # rows = cur.fetchall()
    #
    # def check_topic(self,topic):
    #     with self.conn:
    #         cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
    #         sql = "SELECT DISTINCT event_id,topic FROM event WHERE topic REGEXP '%s'" % topic
    #         cur.execute(sql)
    #         rows = cur.fetchall()
    #         print '查重中',topic
    #         if len(rows) > 1:
    #             eid = rows[0]['event_id']
    #             update = "UPDATE event SET event_id = '%s' WHERE topic = '%s'" % (eid,topic)
    #             cur.execute(sql)
    #             print '发现重复,修改eid中'
    #             return eid
    #         else:
    #             return True
    def delete_event(self,eid):
        """
        爬虫,删除不是热点的事件
        :param eid:
        :return:
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            check = "SELECT * FROM event WHERE event_id='%s'" % eid
            cur.execute(check)
            rows = cur.fetchall()
            if len(rows) == 0:
                pass
            else:
                delete = "DELETE FROM event WHERE event_id='%s'" % eid
                cur.execute(delete)
        return True

    def search_exact_topic(self,topic):
        """
        用于前端搜索框,正则匹配主题,选出对应事件的eid
        :param topic:
        :return:({event_id,etopic},{},...)
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT event_id,etopic FROM event WHERE etopic ='%s' limit 1" % topic
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) == 0:
                rows = ()
                return rows
            else:
                return rows

    def search_vague_topic(self, topic):
        """
        用于前端搜索框,正则匹配主题,选出对应事件的eid
        :param topic:
        :return:({event_id,etopic},{},...)
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT event_id,etopic FROM event WHERE etopic LIKE '%"+topic+"%'"
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) == 0:
                rows = ()
                return rows
            else:
                return rows

    def get_tiemline(self):
        """
        用于时间轴,提取事件与日期
        :return:({'topic': u'111', 'day': 25L, 'month': 4L},)
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            # sql = "SELECT DISTINCT etopic, MONTH( post_time ) AS month, DAY( post_time ) AS day "\
            #         "FROM (SELECT * FROM event WHERE post_time IS NOT NULL GROUP BY DATE(post_time)"\
            #        "ORDER BY post_time DESC LIMIT 12) AS temp GROUP BY etopic ORDER BY post_time ASC  LIMIT 12"
            sql = "SELECT DISTINCT etopic, MONTH( post_time ) AS month, DAY( post_time ) AS day "\
                  "FROM (select * from event natural join networkscale WHERE label_dir !='None' limit 12) as temp"\
                    " GROUP BY DATE(post_time) ORDER BY post_time ASC  LIMIT 12"
            cur.execute(sql)
            rows = cur.fetchall() #({},{}),({'topic': u'111', 'day': 25L, 'month': 4L},)
            # print 'get timeline',rows
            if len(rows) == 0:
                default = ()
                return default
            else:
                return rows

    def get_topic(self,eid):
        """
        按eid提取事件主题,显示于前端linechart页面,network页面title处
        :param eid: event_id
        :return: {'topic':''}
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT etopic FROM event WHERE event_id = '%s'" % eid
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) != 0:
                return rows[0]
            else:
                rows={'etopic':'NO'}
                return rows

