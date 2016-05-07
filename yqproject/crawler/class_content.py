#coding=utf-8
__author__ = 'yc'

from class_save_data import *

class Content(Database):
    def __init__(self):
        Database.__init__(self)

    def get_content(self,eid):
        """
        与save_event_rest共同用于保存爬虫数据到数据库
        :param eid:
        :return:
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT blog_id,post_time FROM content WHERE event_id ='%s' ORDER BY post_time ASC LIMIT 1" % eid
            cur.execute(sql)
            rows = cur.fetchall()
        print "从数据库中提取event_id为",eid,"的记录",rows[0]['post_time']
        return rows[0]

    def save_event_rest(self, rows, tp, tpw, link,eid):
        ptime = rows['post_time']
        print 'post_time', ptime
        origin = rows['blog_id']
        print "正在更新event表"
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "UPDATE event SET post_time='%s',topic='%s',topic_words='%s',origin='%s',link='%s'" \
                  " WHERE event_id ='%s'" % (ptime, tp, tpw, origin, str(link), eid)
            print sql
            cur.execute(sql)

    def get_main_content(self,eid):
        """
        用于提取content表数据到前端,linechart页sidebar
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT content FROM content WHERE event_id = '%s' limit 1" % eid
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) != 0:
                return rows[0]
            else:
                rows={'content':'嚯，百度厉害呀。虚假医疗广告，耽误治疗。他死了，百度说：感谢反馈。真是恶心和令人作呕啊！'}
                return rows

    def get_topic_words(self,eid):
        """
        用于获取事件关键词,用于linechart页sidebar
        :param eid: 事件id
        :return:
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT keywords FROM content WHERE event_id = '%s' limit 1" % eid
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) != 0:
                return rows[0]
            else:
                rows={'keywords':'暂时没有'}
                return rows