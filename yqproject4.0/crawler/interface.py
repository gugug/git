# coding=utf-8
from get_tpw import *
from pack_tbw import *
from class_save_data import *

__author__ = 'gu'

class SaveData:


    # data = pack_tbw()  # return pack_dict, bid_list, title_list, tw_list, ptime_list, content, bid_uiddict

    def __init__(self):
        data = pack_tbw()
        self.pack_dict = data[0]
        self.bid_list = data[1]
        self.title_list = data[2]
        self.tw_list = data[3]
        self.ptime_list = data[4]
        self.content = data[5]
        self.bid_uid = data[6]
        self.db = Database()

    def get_pack_dict(self):
        return self.pack_dict

    def interface_content(self):
        for index in range(len(self.bid_list)):
            blog_id = self.bid_list[index]
            post_time = self.ptime_list[index]
            event_id = 'tp' + self.bid_list[index]  # 既然你要放聚类后面,那就是tp+bid,记得改start topic
            topic = self.title_list[index]
            topic_words = ''  # title的分词
            content = self.content[index]
            keywords = self.tw_list[index]
            self.db.save_content(blog_id, event_id, post_time, topic, topic_words, content, keywords)

    def interface_event(self):

        for keys, values in self.pack_dict.items():
            # 这个是以事件为单位的别弄错
            bid_index = self.bid_list.index(keys)
            event_id = 'tp' + keys  # tp+bid1
            # print 'event_id-----------------------------',event_id
            post_time = self.ptime_list[bid_index] # bid1的post time
            etopic = self.title_list[bid_index]
            origin = self.bid_uid[keys][0]
            link = self.bid_uid[keys][1]
            self.db.save_event(event_id, post_time, etopic, origin, link)

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

    def interface_participate(self):
        for (bid, values) in self.bid_uid.items():  # {bid: (uid,XXX)}
            user_id = values[0]  # 用户,uid,希望你还能对的上
            event_id = 'tp' + bid  # eid,希望你还能对得上号
            # print 'event_id_participate--------------------', event_id
            self.db.save_participate(user_id, event_id)


