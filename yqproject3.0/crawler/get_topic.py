# coding=utf-8
from class_weibo import *
__author__ = 'gu'

"""
5.17 测试完毕
"""

def get_topic(list_key, tuple_value, s):
    """
    爬取博文的主题，【】内的内容
    :param key:list 猎头的id [201783423]
    :param value: 值为(时间,博文,点赞,转发链接,转发量,评论链接,评论量）元组组成的列表
    :param s： 信号量 控制进程中变量的冲突
    :return: weibo_topic, blog_id_list, weibo (tuple)  三个列表的元组， 返回还没有被检测的话题事件
    weibo_topic (list) 表示当前检测到的新话题事件
    blog_id_list (list) 表示当前博文的id
    weibo (list) 表示博文
    """

    weibo_topic = []
    blog_id_list = []
    weibo = []
    print "检测前保存的话题数量为", len(WeiboPage.all_all_topic)
    for i in tuple_value:
        for j in i:
            topic_patternts = re.compile('#(.*?)# |【(.*?)】')
            topic = topic_patternts.findall(j[2])
            if len(topic) > 0:
                topic = topic[0][0] + topic[0][1]
                topic_clean_pattern = re.compile('(\[.*?])')
                topic = re.sub(topic_clean_pattern, '', topic)
                topic_clean2_pattern = re.compile('#(.*?)#')
                topic = [re.sub(topic_clean2_pattern, '', topic)]

                s.acquire()  # 信号量控制
                if topic[0] not in WeiboPage.all_all_topic:  # 对已搜索过的话题进行去除
                    WeiboPage.all_all_topic.append(topic[0])  # 专门保存话题的变量中增加新检测到的话题
                    weibo_topic.append(topic[0])  # 保存只在这次检测过程中发现的话题
                    blog_id_list.append(j[1])  # 保存每个新事件的bid
                    weibo.append(j[2])  # 保存发现新事件的原文博文
                else:
                    print "该话题不属于新检测到的事件", topic[0]
                s.release()
            else:
                print "这篇博文没有话题，检测不到事件"

    print "检测到的新事件数量", len(weibo_topic)

    for ntopic in weibo_topic:
        print list_key,"检测到的新事件", ntopic

    print "保存到的话题最新数量", len(WeiboPage.all_all_topic)
    for stopic in WeiboPage.all_all_topic:
        print "保存的话题有：", stopic
    return weibo_topic, blog_id_list, weibo
