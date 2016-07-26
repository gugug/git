# coding=utf-8
from pack_tbw import *
from get_keyword.get_keyword import *
__author__ = 'gu'

# def get_keywords():
#     bbw_dict = {}
#     bb_dict = cluster()   # {bid1:[blog1,blog2,blog3]， bid2:[blog4,blog5,blog6]}
#     for bid, events in bb_dict.items():
#         for blog in events:
#             word = Keyword().combine_keywords(blog)  # 博文的关键词提取
#             bbw_dict.setdefault(bid,[]).append(word)
#     return bbw_dict  # {bid1:[word1,word2,word3]， bid2:[word4,word5,word6]}