# coding=utf-8
from crawl_weibo import *
from combine.text_analyse import *
from get_tpw import *

__author__ = 'gu'
"""
5.28 测试完毕
"""

def pack_tbw():
    """
    get_tpw 提取标题和关键字
    title_cluster 进行标题的聚类
    :return: pack_dict,聚类后的字典 {bid1:[(title1,blog1,word1),(title1,blog2,word2)], bid2:[(title2,blog4,word4)]}

    """
    pack_dict = {}
    bid_uiddict = {}
    print "全局的长度,表示猎头数", len(WeiboPage.all_hunterlist)
    for one_dict in WeiboPage.all_hunterlist:
        for (keys, values) in one_dict.items():
            for j in values:
                content_ptime = [j[2], j[0]]  # [博文 ,时间]
                WeiboPage.detected_tpdict.setdefault(j[1], content_ptime)  # 我把博文id作为键，
                bid_uiddict.setdefault(j[1], [keys, j[8]])

    print "字典长度", len(WeiboPage.detected_tpdict)

    bid_list, title_list, tw_list, ptime_list, content = get_tpw(WeiboPage.detected_tpdict)

    index_result = title_cluster(title_list)  # 聚类返回索引

    for com in index_result:
        print "该类的代表bid 标题 博文关键字 发表时间", bid_list[com[0]], title_list[com[0]], tw_list[com[0]], ptime_list[com[0]], content[com[0]]
        for bid_index in com:
            # bid = bid_list[bid_index]
            print "         ", bid_list[bid_index], title_list[bid_index], tw_list[bid_index], ptime_list[bid_index], content[bid_index]
            # print "         ", bid, WeiboPage.detected_tpdict[bid][0], WeiboPage.detected_tpdict[bid][1]  # 一个类的id,代表性的博文，及其发表时间
            # tbw_tuple = (title_list[com[0]], WeiboPage.detected_tpdict[bid], tw_list[bid_index])  # （固定第一个的标题，博文，关键词）
            tbw_tuple = (title_list[com[0]], content[bid_index], tw_list[bid_index])
            pack_dict.setdefault(bid_list[com[0]], []).append(tbw_tuple)

    print "话题聚类完毕"

    return pack_dict, bid_list, title_list, tw_list, ptime_list, content, bid_uiddict
