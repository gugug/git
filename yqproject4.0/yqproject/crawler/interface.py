# coding=utf-8
from get_tpw import *
from pack_tbw import *

__author__ = 'gu'

class SaveDate:

    data = pack_tbw()  # return pack_dict, bid_list, title_list, tw_list, ptime_list, content, bid_uiddict

    def __init__(self):
        self.pack_dict = self.data[0]
        self.bid_list = self.data[1]
        self.title_list = self.data[2]
        self.tw_list = self.data[3]
        self.ptime_list = self.data[4]
        self.content = self.data[5]
        self.bid_uid = self.data[6]

    def interface_content(self):
        for index in range(len(self.bid_list)):
            blog_id = self.bid_list[index]
            post_time = self.ptime_list[index]
            event_id = 'tp' + self.bid_list[index]  # 既然你要放聚类后面,那就是tp+bid,记得改start topic
            topic = self.title_list[index]
            topic_words = ''  # title的分词
            content = self.content[index]
            keywords = self.tw_list[index]

    def interface_event(self):
        for keys, values in self.pack_dict().items:
            # 这个是以事件为单位的别弄错
            bid_index = self.bid_list.index(keys)
            event_id = 'tp' + keys  # tp+bid1
            post_time = self.ptime_list[bid_index] # bid1的post time
            etopic = self.title_list[bid_index]
            origin = self.bid_uid[keys][0]
            link = self.bid_uid[keys][1]

    # def interface_networkscale():  # 多进程的原因，我把它写在了start_search()里
    #     event_id =
    #     corpus_dir = 语料路径
    #     label_dir = label路径
    #     sna_dir = sna图的路径,这个你可以留空
    #     leader = 留空

    # def interface_increment():  # 多进程的原因，我把它写在了start_search()里
    #     这个很欣慰,可以完全对应你的 start_search() bid_like, bid_forward, bid_comment
    #     event_id =
    #     check_time =
    #     comment_num =
    #     repost_num =
    #     like_num =

    def participate(self):
        for (bid, values) in self.bid_uid:
            user_id = values[0]  # 用户,uid,希望你还能对的上
            event_id = 'tp' + bid  # eid,希望你还能对得上号


