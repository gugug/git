# coding=utf-8
from pack_tbw import *
from search_topic import SearchTopic as st
import shutil
from interface import *

__author__ = 'gu'
"""
5.28 测试完毕
"""


def muL_ss():
    """
    多进程进行开始搜索搜索，多进程调用start_search
    :return:
    """

    tbw_dict = SaveDate().data[0]
    # {bid1:[(title1,blog1,word1),(title2,blog2,word2)], bid2:[(title4,blog4,word4),(title5,blog5,word5)]}
    for (bid, tbw_list) in tbw_dict.items():
        search_process = multiprocessing.Process(target=start_search, args=(bid, tbw_list))  # 一个bid作为一个进程搜索
        search_process.start()
    search_process.join()


def start_search(bid, tbw_list):
    """
    经过聚类后便可以开始搜索， 进行st().search_topic搜索，生成文件夹，如果不是热点的话题，便删除文件夹
    :param bid: 每一个类的代表博文id
    :param tbw_list: 这个类的博文相关属性的组合， [(title1,blog1,word1),(title2,blog2,word2)]
    :return:
    """
    e_id = 'tp' + bid
    short_dir = create_time_file(tbw_list[0][0])  # 创建标题文件夹
    corpus_dir = DOC_DIR + '/' + short_dir + 'uid=' + str(bid) + '.txt'
    print "生成的动态目录：", corpus_dir
    txt_file = open(corpus_dir, 'w+')

    bid_like = 0  # 该bid类的点赞规模
    bid_forward = 0
    bid_comment = 0

    for tbw_tuple in tbw_list:  # [(title1,blog1,word1),(title2,blog2,word2)]
        print bid, "类的博文标题, 博文, 关键词", tbw_tuple[0], tbw_tuple[1], tbw_tuple[2]

        total_result_list, total_reason_list, lfc_all_num = st().search_topic(bid, tbw_tuple)

        # total_result_list = [[博文id,博文时间,标题,博文,关键词,首发者的id,首发者的名字,点赞,转发,评论,origin], ]
        for com_index in range(len(total_result_list)):
            for com in total_result_list[com_index]:
                txt_file.write(str(com) + '\n')

            # total_reason_list = [[古阿陌@洗洗睡@人民日报, 南方报@人民日报, yutsfa@人民日报 ], ]
            for reason in total_reason_list[com_index]:
                print "转发理由：", reason
                txt_file.write(str(reason) + '\n')
            txt_file.write('\n')
        txt_file.write('\n\n\n--------------------\n')

        # lfc_all_num = [该话题的点赞规模,该话题的转发规模,该话题的评论规模]
        print '*******************************'
        print "该话题的点赞规模", lfc_all_num[0]
        print "该话题的转发规模", lfc_all_num[1]
        print "该话题的评论规模", lfc_all_num[2]

        bid_like += int(lfc_all_num[0])
        bid_forward += int(lfc_all_num[1])
        bid_comment += int(lfc_all_num[2])

    print tbw_list[0][0], '聚合的类的话题规模', bid_like, bid_forward, bid_comment

    txt_file.write(str(bid_like) + '\n' +
                   str(bid_forward) + '\n' +
                   str(bid_comment) + '\n')
    txt_file.close()
    if bid_like + bid_forward + bid_comment == 0:
        deleted_dir = DOC_DIR + '/' + 'topic' + '/' + tbw_list[0][0]
        print "不是热点的文件夹删除", deleted_dir
        shutil.rmtree(deleted_dir)

    else:
        now = datetime.datetime.now()
        other_style_time = now.strftime("%Y-%m-%d %H:%M:%S")

    #  存 interface_networkscale():
        event_id = e_id
        corpus_dir = short_dir

        label_dir = label路径
        sna_dir = sna图的路径,这个你可以留空
        leader = 留空

    # 存 interface_increment():
        check_time = other_style_time
        comment_num = bid_comment
        repost_num = bid_forward
        like_num = bid_like
