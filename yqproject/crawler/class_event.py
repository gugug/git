#coding=utf-8
__author__ = 'yc'

from class_save_data import *


class Event(Database):
    def __init__(self):
        Database.__init__(self)

    def save_event_id(self,eid):
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "Replace INTO event(event_id) VALUES ('%s')" % eid
            cur.execute(sql)
            # rows = cur.fetchall()

    def check_topic(self,topic):
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT event_id FROM event WHERE topic = '%s'" % topic
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) > 1:
                eid = rows[0]['event_id']
                update = "UPDATE event SET event_id = '%s' WHERE topic = '%s'" % (eid,topic)
                cur.execute(sql)
                print '发现重复,修改eid中'
                return eid
            else:
                return True

    def search_topic(self, topic):
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT event_id FROM event WHERE topic LIKE '%"+topic+"%'"
            cur.execute(sql)
            rows = cur.fetchall()
            print rows
            if len(rows) == 0:
                event_id = '000' #表示没找到
            else:
                event_id = rows[0]['event_id']
            print event_id
            return event_id

    def get_topic(self): #用于时间轴
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT topic, MONTH( post_time ) AS month, DAY( post_time ) AS day "\
                    "FROM (SELECT * FROM event WHERE post_time IS NOT NULL GROUP BY DATE(post_time)"\
                   "ORDER BY post_time DESC LIMIT 15) AS temp GROUP BY topic ORDER BY post_time ASC  LIMIT 15"
            cur.execute(sql)
            rows = cur.fetchall() #({},{}),({'topic': u'111', 'day': 25L, 'month': 4L},)
            print rows
            if len(rows) == 0:
                default = False
                return default
            else:
                return rows

    def get_topic_by_id(self,eid):
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT topic FROM event WHERE event_id = '%s'" % eid
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) != 0:
                return rows[0]
            else:
                rows={'topic':'NO'}
                return rows
    def get_topic_words(self,eid):
         with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT topic_words FROM event WHERE event_id = '%s'" % eid
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) != 0:
                return rows[0]
            else:
                rows={'topic_words':'NO'}
                return rows