# coding=utf-8
__author__ = 'gu'
from class_weibo import *
from search_topic import *
class Update(WeiboPage):
    """
    更新器，更新之前检测到的话题时间，进行重新更新规模
    """
    def update(self):
        """
        更新之前检测到的话题
        :return:
        """
        print "即将开始检测....."
        for uid, afore_tuple_list in WeiboPage.afore_all_uid.items():
            for afore_tuple in afore_tuple_list:
                update_process = multiprocessing.Process(target=SearchTopic(self.one_user).get_search_topic, args=(uid, afore_tuple))
                update_process.start()
            update_process.join()
        print "全部话题更新完毕，开始再次检测新事件"