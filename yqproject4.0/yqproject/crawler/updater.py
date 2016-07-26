# coding=utf-8
from search_topic import *

__author__ = 'gu'

# def update():
#     """
#     更新之前检测到的话题
#     :return:
#     """
#     print "即将开始检测....."
#     for uid, searched_tuple_list in WeiboPage.searched_tpdict.items():
#         for searched_tuple in searched_tuple_list:
#             update_process = multiprocessing.Process(target=SearchTopic().search_topic, args=(uid, searched_tuple))
#             update_process.start()
#         update_process.join()
#     print "全部话题更新完毕，开始再次检测新事件"