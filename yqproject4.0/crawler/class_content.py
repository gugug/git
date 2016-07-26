#coding=utf-8
__author__ = 'yc'

from class_save_data import *
from crawl_weibo import *
class Content(Database):
    def __init__(self):
        Database.__init__(self)

    def get_exist_topic(self):
        """
        取出已存在数据库中的主题,以便进行判重
        :return:True
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT topic from content"
            cur.execute(sql)
            rows = cur.fetchall() #({topic:})
            for i in rows:
                WeiboPage.exist_topic.append(i['topic'])
        return True

    def get_topic_words(self):
        """
        取关键词用于爬虫搜索
        :param bid: blog_id
        :return:要输入搜索框的关键词的列表
        """
        tpw_list = []
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT topic_words from content"
            cur.execute(sql)
            rows = cur.fetchall() #({},{})
            if len(rows) == 0:
                return tpw_list
            for i in rows:
                tpw_list.append(i['topic_words'])
        return tpw_list

    def get_topic_tuple(self,):
        """
        用于爬虫存储过程中的事件聚类
        :return:({'blog_id':'','topic':'','topic_words':''})
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT blog_id, topic, topic_words from content WHERE event_id is NULL "
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) == 0:
                return False
            else:
                return rows


    def get_content(self,eid):
        """
        用于提取content表数据到前端,linechart页sidebar
        :param eid:event_id
        :return:{'content':'' }
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT content FROM content WHERE event_id = '%s' limit 1" % eid
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) != 0:
                return rows[0]
            else:
                rows={'content':'暂时没有'}
                return rows

    def get_keywords(self,eid):
        """
        用于获取事件关键词,用于linechart页sidebar
        :param eid: 事件id
        :return:{'keywords':''}
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



    # def get_content(self,eid):
    #     """
    #     与save_event_rest共同用于保存爬虫数据到数据库
    #     :param eid:
    #     :return:
    #     """
    #     with self.conn:
    #         cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
    #         sql = "SELECT blog_id,post_time FROM content WHERE event_id ='%s' ORDER BY post_time ASC LIMIT 1" % eid
    #         cur.execute(sql)
    #         rows = cur.fetchall()
    #     print "从数据库中提取event_id为",eid,"的记录",rows[0]['post_time']
    #     return rows[0]
    #
    # def save_event_rest(self, rows, tp, tpw, link,eid):
    #     ptime = rows['post_time']
    #     print 'post_time', ptime
    #     origin = rows['blog_id']
    #     print "正在更新event表"
    #     with self.conn:
    #         cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
    #         sql = "UPDATE event SET post_time='%s',topic='%s',topic_words='%s',origin='%s',link='%s'" \
    #               " WHERE event_id ='%s'" % (ptime, tp, tpw, origin, str(link), eid)
    #         print sql
    #         cur.execute(sql)