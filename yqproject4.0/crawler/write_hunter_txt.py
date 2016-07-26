# coding=utf-8
__author__ = 'gu'
"""
5.17 测试完毕
"""
import os
from class_content import *

def write_hunter_txt(key, value):
    """
    写猎头的博文txt备份 —— uid,时间,博文id,博文,点赞,转发链接,转发量,评论链接,评论量,新闻源
    :param key: 字典的键，即是uid
    :param value: 值为(时间,博文,点赞,转发链接,转发量,评论链接,评论量）元组组成的列表
    :return:
    """
    
    hunter_dir = os.path.join(BASE_DIR, 'documents', 'hunter_weibo')
    print '正在写入用户', key, '博文'
    for i in value:
        # print "value", value
        # print key[0], "今天发的博文数量", len(i)
        now = datetime.datetime.now()
        other_style_time = now.strftime("%Y-%m-%d")

        time_hunter = hunter_dir + '/' + other_style_time
        if os.path.exists(time_hunter):
            pass
        else:
            os.mkdir(time_hunter)
            
        hunter_txt = open(time_hunter + '/' + 'uid=' + str(key[0]) + '.txt', 'w+')
        for j in i:
            # print "id,时间,博文id,博文,点赞,转发链接,转发量,评论链接,评论量,新闻源", key[0], j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], \
            #     j[8]
            hunter_txt.write(
                str(key[0])
                + "\n发表时间 " + str(j[0])
                + "\n博文id： " + str(j[1])
                + "\n博文： " + str(j[2])
                + "\n点赞量： " + str(j[3])
                + "\n转发链接： " + str(j[4])
                + "\n转发量： " + str(j[5])
                + "\n评论链接 ： " + str(j[6])
                + "\n评论量： " + str(j[7])
                + "\n新闻源： " + str(j[8])
                + '\n\n')
                # blog_id = str(j[0])
                # ptime = str(j[1])
                # content = str(j[])
        hunter_txt.close()
    print '完成用户', key, '的博文存储'


