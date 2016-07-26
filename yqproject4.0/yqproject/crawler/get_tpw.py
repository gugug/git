# coding=utf-8
from crawl_weibo import *
from get_keyword.get_keyword import *

__author__ = 'gu'
"""
5.28 测试完毕
"""

# def interface_content(tuple):
#     """
#     处理传入的字典元组:{id:(时间,博文,点赞,转发链接,转发量,评论链接,评论量）}
#     :param tuple: {id:(时间,博文,点赞,转发链接,转发量,评论链接,评论量）}
#     :return: no return, 存入数据库
#     """
#     topic_list = []
#     for i in tuple:  # tuple:[()]
#         for j in i:
#             bid = str(j[0])
#             ptime = str(j[1])
#             content = str(j[2])
#             like_num = str(j[3])
#             forward_path = str(j[4])
#             repost_num = str(j[5])
#             comment_link = str(j[6])
#             comment_num = str(j[7])
#             origin = str(j[8])
#
#             topic_patternts = re.compile('【(.*?)】')
#             topic = topic_patternts.findall(j[2])
#             if len(topic) > 0:
#                 topic_clean_pattern = re.compile('(\[.*?])')
#                 topic = re.sub(topic_clean_pattern, '', topic[0])
#                 topic_clean2_pattern = re.compile('#(.*?)#')
#                 topic = re.sub(topic_clean2_pattern, '', topic)
#             else:
#                 print "这篇博文没有话题，检测不到事件"
#             kw = Keyword()
#             key_words = kw.combine_keywords(content)
#             topic_words = kw.combine_keywords(topic)
#             Database().save_content(bid, ptime, topic, topic_words, content, key_words)
#             topic_list.append(topic)
#     return topic_list
#
#
# def interface_is_exist(topic_list):  ##待改进,争议中
#     """
#     对话题进行判重
#     :param topic_list: 话题列表
#     :return: 未搜索过的话题
#     """
#     unsearched_topic = []
#     for topic in topic_list:
#         result = Content().get_exist_topic(topic)
#         if result == False:
#             unsearched_topic.append(topic[0])
#     return unsearched_topic

def get_tpw(tpdict):

    """
    提取标题和 博文关键字
    :param tpdict: {bid1:[blog1, ptime], }
    :return: 四个列表
    """

    bid_list = []
    title_list = []
    tw_list = []
    ptime_list = []
    content_list = []
    for (keys, values) in tpdict.items():
        print "博文id", keys, "博文", values[0], "发表时间", values[1]
        topic_patternts = re.compile('【(.*?)】')
        topic = topic_patternts.findall(values[0])
        if len(topic) > 0 and topic not in title_list:
            topic_clean_pattern = re.compile('(\[.*?])')
            topic = re.sub(topic_clean_pattern, '', topic[0])
            topic_clean3_pattern = re.compile('#')
            topic = re.sub(topic_clean3_pattern, '', topic)
            topic_clean2_pattern = re.compile('\\s')
            topic = re.sub(topic_clean2_pattern, '', topic)

            word = Keyword().combine_keywords(values[0])

            bid_list.append(keys)
            title_list.append(topic)
            tw_list.append(word)
            ptime_list.append(values[1])
            content_list.append(values[0])

        else:
            print "这篇博文没有话题，检测不到事件"

    return bid_list, title_list, tw_list, ptime_list, content_list

