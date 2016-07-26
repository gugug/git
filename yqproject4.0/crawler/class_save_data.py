# -*- coding: UTF-8 -*-
"""
4.2 测试完成
"""
__author__ = 'yc'

import MySQLdb
import datetime
import re
import _mysql_exceptions

class Database:
    """
    操作数据库的父类,主要用于存储数据,对特定表数据使用的类将继承此父类
    """

    def __init__(self):
        self.conn = MySQLdb.connect(
            host='42.96.134.205',  # 192.168.235.36 fig #192.168.1.41 me #192.168.1.40 jie
            port=3306,
            user='root',
            passwd='ViveMax2016',
            db='yuqing',
            charset='utf8', )
        now = datetime.datetime.now()
        self.ctime = datetime.datetime.replace(now, minute=0, second=0, microsecond=0)
        self.ltime = datetime.datetime.now() - datetime.timedelta(hours=1)  # 暂时无用

    def save_increment(self, eid, comment=0, repost=0, like=0):
        """
        向事件描述表添加数据
        :param eid: 事件id
        :param comment: 评论数
        :param repost: 转发数
        :param like: 点赞数
        :return:
        """
        try:
            with self.conn:
                cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
                insert = "INSERT INTO increment(event_id,check_time,comment_num,repost_num,like_num) " \
                         "VALUES('%s','%s','%s','%s','%s')" % (eid, self.ctime, comment, repost, like)
                print insert
                cur.execute(insert)
                print '数据已存入事件描述表'
            return True
        except _mysql_exceptions.IntegrityError:
            print "外键约束"
        except:
            pass


    def save_network_scale(self, eid, cps='None', label='None', sna='None', leader='Unknown'):
        """
        向网络规模表添加数据
        :param topic: 主题
        :param cps: 语料库
        :param sna: sna.png路径
        :param label: label.xls路径
        :param leader: 核心人物
        :return:
        """
        try:
            with self.conn:
                cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
                insert = "REPLACE INTO networkscale" \
                         "(event_id,check_time,corpus_dir,label_dir,sna_dir,leader)" \
                         " VALUES('%s','%s','%s','%s','%s','%s')" % \
                         (eid, self.ctime, cps, label, sna, leader)
                cur.execute(insert)
                print '数据已存入网络规模表'
            return True
        except _mysql_exceptions.IntegrityError:
            print "外键约束"
        except:
            pass

    def save_event(self, eid, ptime, etopic, origin, link):
        """
        写第n次存event表的函数了,宝宝心累
        :param eid: 事件id
        :param ptime: 首发时间
        :param etopic: 话题
        :param origin: 传播源
        :param link: 链接
        :return:
        """
        try:
            pptime = str(ptime)
            date = re.search('(\d+)月(\d+)日', pptime)
            time = re.search('(\d+):(\d+)', pptime)
            if time is not None:
                hour = int(time.group(1))
                minute = int(time.group(2))
            else:
                hour = 0
                minute = 0
            ptime = datetime.datetime(2016, int(date.group(1)), int(date.group(2)), hour, minute)
            with self.conn:
                cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
                check = "select * from event where event_id='%s'" % eid
                cur.execute(check)
                rows = cur.fetchall()
                if len(rows) == 0:
                    insert = "INSERT INTO event" \
                             "(event_id,post_time,etopic,origin,link)" \
                             " VALUES('%s','%s','%s','%s','%s')" % \
                             (eid, ptime, etopic, origin, link)
                    cur.execute(insert)
                    print '数据已存入网络规模表'
                else:
                    print '数据已存在'
            return True
        except _mysql_exceptions.IntegrityError:
            print "外键约束"
        except:
            pass


    def save_headhunter(self, uid, name, gender='Unknown', bir='0000-00-00', vip='Unknown', loc='Unknown', pro='Unknown', tag='Unknown',
                        fans=0, fol=0, blog=0):
        """
        向猎头信息表添加数据
        :param uid: 用户id
        :param name: 昵称
        :param gender: 性别
        :param bir: 生日
        :param vip: 认证信息
        :param loc: 地区
        :param pro: 简介
        :param tag: 标签
        :param fans: 粉丝书
        :param fol: 关注数
        :param blog: 微博数
        :return:
        """
        bir = str(bir)
        year = re.search('\d{4}', bir)
        if year is None:
            bir = '0000-' + bir
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            insert = "REPLACE INTO headhunter" \
                     "(user_id,user_name,gender,birth,vip_state,location,profile,tag,fans_num,follow_num,blog_num)" \
                     " VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                     (uid, name, gender, bir, vip, loc, pro, tag, fans, fol, blog)
            cur.execute(insert)
            print '数据已存入猎头信息表'
        return True

    def save_participate(self, uid, eid):
        """
        向人物事件关系表添加数据
        :param uid: 用户id
        :param eid: 事件id
        :return:
        """
        try:
            with self.conn:
                cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
                check1 = "select * from event where event_id='%s'" % eid
                cur.execute(check1)
                rows = cur.fetchall()
                if len(rows) != 0:
                    insert = "REPLACE INTO participate (user_id, event_id) VALUES('%s','%s')" % (uid, eid)
                    cur.execute(insert)
                    print "数据已存入参与关系表"
                else:
                    print eid,"不是热点事件"
            return True
        except _mysql_exceptions.IntegrityError:
            print "外键约束"
        except:
            pass

    def save_content(self, bid, eid, ptime, tp, tpw, cnt, kw):
        """
        向事件内容表添加数据
        :param bid: 博文id
        :param eid: 事件id
        :param cnt: 博文内容
        :param ptime: 博文发表时间
        :param tp: 博文主题
        :param tpw: 博文主题关键词
        :param kw: 博文内容分词
        :return:
        """
        try:
            pptime = str(ptime)
            date = re.search('(\d+)月(\d+)日', pptime)
            time = re.search('(\d+):(\d+)', pptime)
            if time is not None:
                hour = int(time.group(1))
                minute = int(time.group(2))
            else:
                hour = 0
                minute = 0
            ptime = datetime.datetime(2016, int(date.group(1)), int(date.group(2)), hour, minute)

            with self.conn:
                cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
                check = "select * from content where event_id='%s'" % eid
                cur.execute(check)
                rows = cur.fetchall()
                if len(rows) == 0:
                # check1 = "SELECT blog_id from content where blog_id='%s' or topic='%s'" % bid, tp
                    insert = "REPLACE INTO content (blog_id,post_time, event_id, topic, topic_words, content, keywords) " \
                         "VALUES('%s','%s','%s','%s','%s','%s','%s')" % (bid, ptime, eid, tp, tpw, cnt, kw)
                    cur.execute(insert)
                    print "数据已存入事件内容表"
                else:
                    print "数据已存在"
            return True
        except _mysql_exceptions.IntegrityError:
            print "外键约束"
        except:
            pass

    def update_eid(self, bid, eid):
        """
        聚类后给博文标上所属事件id
        :param bid: blog_id
        :param eid: event_id
        :return:
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "UPDATE content SET event_id='%s' WHERE blog_id='%s'" % (eid, bid)
            cur.execute(sql)
            print "博文按事件归类完成"

    # def save_event(self, eid):
    #     """
    #     从content表中取出已聚类的事件,把eid,最早发布时间,主题存入event表
    #     :param eid: event_id
    #     :return:
    #     """
    #     with self.conn:
    #         cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
    #         sql = "SELECT DISTINCT event_id, post_time,topic from content WHERE event_id = '%s' " \
    #               "ORDER BY post_time ASC LIMIT 1" % eid
    #         insert = "into event(event_id, post_time, etopic)"
    #         cur.execute(sql + insert)
    #         print "数据已存入热门事件表"
    #     return True
    #
    # def update_event(self, eid, origin, link):
    #     with self.conn:
    #         cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
    #         sql = "update event SET origin='%s',link='%s' WHERE event_id ='%s'" % (origin, link, eid)
    #         cur.execute(sql)
    #         print "已更新热门事件表"
    #     return True

    # def save_event(self, eid, ptime, topic='未知', origin='未知', link='未知'):
    #     """
    #     向爬取微博表添加数据
    #     :param eid: 事件id
    #     :param ptime: 发表时间
    #     :param topic: 事件主题
    #     :param origin: 传播源
    #     :param link: 新闻链接
    #     :return:
    #     """
    #
    #     pptime = str(ptime)
    #     date = re.search('(\d+)月(\d+)日', pptime)
    #     time = re.search('(\d+):(\d+)', pptime)
    #     if time is not None:
    #         hour = int(time.group(1))
    #         minute = int(time.group(2))
    #     else:
    #         hour = 0
    #         minute = 0
    #     ptime = datetime.datetime(2016, int(date.group(1)), int(date.group(2)), hour, minute)
    #
    #     with self.conn:
    #         cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
    #         insert = "REPLACE INTO event(event_id,post_time,etopic,origin,link)" \
    #                  " VALUES('%s','%s','%s','%s','%s')" % (eid, ptime, topic, origin, link)
    #         cur.execute(insert)
    #         print '数据已存入爬取微博表'
    #     return True
# a = Database().conn