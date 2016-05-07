# -*- coding: UTF-8 -*-
"""
4.2 测试完成
"""
__author__ = 'yc'

import MySQLdb
import datetime
import re


class Database:
    """
    操作数据库的父类,主要用于存储数据,对特定表数据使用的类将继承此父类
    """

    def __init__(self):
        self.conn = MySQLdb.connect(
            host='127.0.0.1',  # 192.168.235.36 fig #192.168.1.41 me #192.168.1.40 jie
            port=3306,
            user='yc',
            passwd='uliuli520',
            db='yuqing',
            charset='utf8', )
        self.ctime = datetime.datetime.now()
        self.ltime = datetime.datetime.now() - datetime.timedelta(hours=1)

    def save_increment(self, eid, comment=0, repost=0, like=0):
        """
        向事件描述表添加数据
        :param eid: 事件id
        :param comment: 评论数
        :param repost: 转发数
        :param like: 点赞数
        :return:
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            insert = "INSERT INTO increment(event_id,check_time,comment_num,repost_num,like_num) " \
                     "VALUES('%s','%s','%s','%s','%s')" % (eid, self.ctime, comment, repost, like)
            print insert
            cur.execute(insert)
            print '数据已存入事件描述表'
        return True

    def save_network_scale(self, eid, cps='未知', label='未知', leader='未知'):
        """
        向网络规模表添加数据
        :param topic: 主题
        :param cps: 语料库
        :param data: data.xls路径
        :param label: label.xls路径
        :param leader: 核心人物
        :return:
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            insert = "REPLACE INTO networkscale" \
                     "(event_id,check_time,corpus_dir,label_dir,leader)" \
                     " VALUES('%s','%s','%s','%s','%s')" % \
                     (eid, self.ctime, cps, label, leader)
            cur.execute(insert)
            print '数据已存入网络规模表'
        return True

    def save_event(self, eid, ptime, topic='未知', tpw='未知', origin='未知', link='未知'):
        """
        向爬取微博表添加数据
        :param eid: 事件id
        :param ptime: 发表时间
        :param topic: 主题
        :param tpw: 主题词
        :param origin: 传播源
        :param link: 新闻链接
        :return:
        """

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
            insert = "REPLACE INTO event(event_id,post_time,topic,topic_words,origin,link)" \
                     " VALUES('%s','%s','%s','%s','%s','%s')" % (eid, ptime, topic, tpw, origin, link)
            cur.execute(insert)
            print '数据已存入爬取微博表'
        return True

    def save_headhunter(self, uid, name, gender='未知', bir='0000-00-00', vip='非认证用户', loc='未知', pro='未添加', tag='无',
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
            bir = '0000-'+bir
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
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            insert = "REPLACE INTO participate (user_id, event_id) VALUES('%s','%s')" % (uid, eid)
            cur.execute(insert)
        return True

    def save_content(self, bid, ptime, eid, cnt, kw):
        """
        向事件内容表添加数据
        :param bid: 博文id
        :param eid: 事件id
        :param cnt: 事件内容
        :return:
        """
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
            insert = "REPLACE INTO content (blog_id,post_time, event_id, content, keywords) " \
                     "VALUES('%s','%s','%s','%s','%s')" % (bid, ptime, eid, cnt,kw)
            cur.execute(insert)
        return True

# print type(Database().conn)