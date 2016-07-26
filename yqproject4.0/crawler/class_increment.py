# coding=utf-8
"""
2016.3.24,获取微博评论,转发,点赞数的增量,
"""
__author__ = 'yc'

from crawler.class_save_data import *


class Increment(Database):
    """
    继承Database类,对increment表的操作
    """

    def __init__(self):
        Database.__init__(self)
        self.delta_comment = 0
        self.delta_repost = 0
        self.delta_like = 0
        self.comment_list = []
        self.repost_list = []
        self.like_list = []
        self.time_list = []
        self.comment_rate = []
        self.repost_rate = []
        self.like_rate = []
        self.scale_rate = []

    def get_data(self, eid):
        """从数据库中读取某id的增量数据,返回时间列表和取出的数据"""
        with self.conn:
            flag = False
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            # num_sql = "SELECT COUNT(event_id) AS c,MAX(iid) AS b,Min(iid) AS s From increment WHERE event_id='%s'" % (eid)
            # cur.execute(num_sql)
            # num = cur.fetchall()[0]
            # print 'num',num
            # biggest = num['b']
            # smallest = num['s']
            # count = num['c']
            # if count < 4:
            #     rows = []
            #     return rows
            # if count > 10:
            #     smallest = biggest - 11
            select = "select iid,Hour(check_time) AS hour,comment_num, repost_num," \
                     " like_num from (select * from increment where event_id = '%s' order by iid desc limit 11) as temp order by hour asc" % eid
            # select = "SELECT iid,check_time,Hour(check_time) AS hour, MIN(check_time) As min, comment_num, repost_num, like_num FROM (select * from increment WHERE iid BETWEEN %s AND %s" % (smallest, biggest)
            print select
            cur.execute(select)
            rows = cur.fetchall()  # ({'check_time': datetime.datetime(2016, 3, 26, 19, 4), 'comment_num': 1575L},)
            # print 'rows',rows
            dist_rows=[rows[0]]
            for i in range(1,len(rows)):
                if rows[i]['hour'] != rows[i-1]['hour']:
                    dist_rows.append(rows[i])
                else:
                    pass
            # print dist_rows
            if len(dist_rows) <4:
                rt_rows=[]
                return rt_rows
            for i in range(len(dist_rows) - 1):
                delta_comment = dist_rows[i+1]['comment_num'] - dist_rows[i]['comment_num']
                delta_repost = dist_rows[i+1]['repost_num'] - dist_rows[i]['repost_num']
                delta_like = dist_rows[i+1]['like_num'] - dist_rows[i]['like_num']
                delta_all_num = delta_comment+delta_like+delta_repost
                delta_time = dist_rows[i+1]['hour']-dist_rows[i]['hour']
                scale_rate = delta_all_num/delta_time
                # print 'ddd',delta_all_num,scale_rate
                self.scale_rate.append(str(scale_rate))
                xaxis = str(dist_rows[i+1]['hour'])+':00'
                self.time_list.append(xaxis)  # 以后来的时间为横轴坐标
            # print 'x轴', self.time_list
            # print '数据', self.scale_rate
            return dist_rows



    def get_comment(self,eid):
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT comment_num FROM increment WHERE event_id = '%s' limit 1" % eid
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) != 0:
                return rows[0]
            else:
                rows={'comment_num':'567'}
                return rows

    def get_repost(self,eid):
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT repost_num FROM increment WHERE event_id = '%s' limit 1" % eid
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) != 0:
                return rows[0]
            else:
                rows={'repost_num':'362'}
                return rows

    def get_like(self,eid):
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT like_num FROM increment WHERE event_id = '%s' limit 1" % eid
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) != 0:
                return rows[0]
            else:
                rows={'like_num':'432'}
                return rows

    #   def get_comment1(self, rows):
    #     """计算评论增量,返回评论数据列表"""
    #     for i in range(len(rows) - 1):  # i begins from 0
    #         delta_comment = rows[i + 1]['comment_num'] - rows[i]['comment_num']
    #         delta_time = rows[i+1]['post_time']-rows[i]['post_time']
    #         comment_rate = delta_comment/delta_time
    #         self.comment_rate.append(comment_rate)
    #         self.comment_list.append(delta_comment)
    #         print self.comment_list
    #
    #     return True
    #
    # def get_repost1(self, rows):
    #     """计算转发增量,返回转发数据列表"""
    #     for i in range(len(rows) - 1):
    #         delta_repost = rows[i + 1]['repost_num'] - rows[i]['repost_num']
    #         self.repost_list.append(delta_repost)
    #         print self.repost_list
    #     return True
    #
    # def get_like1(self, rows):
    #     """计算点赞增量,返回点赞数据列表"""
    #     for i in range(len(rows) - 1):
    #         delta_like = rows[i + 1]['like_num'] - rows[i]['like_num']
    #         self.like_list.append(delta_like)
    #         print self.like_list
    #     return True