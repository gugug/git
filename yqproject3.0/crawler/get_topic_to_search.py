# coding=utf-8
from class_weibo import *
from get_hunter_weibo import *
from write_hunter_txt import *
from get_topic import *
from search_topic import *
__author__ = 'gu'
"""
5.17 测试完毕
"""
class SaveTopicToSearch(WeiboPage):
    """
    猎头中的博文信息，通过get_topic获得 三个列表元组-(话题, id, 博文),然后进行关键字的提取Keyword().combine_keywords，
    最终保存在 WeiboPage.afore_all_uid，保存的同时进行此次检测到的话题事件进行搜索
    """
    def save_topic_to_search(self, p1, p2, s):
        """
        调用全部方法，相当于控制器
        爬取博文的方法 one_id_text()
        保存猎头当天发表的博文和博转评方法：write_text()
        爬取猎头微博的评论内容： get_comment()
        爬取猎头的微博的转发路径方法： get_forward_path()
        搜索话题爬取话题相关微博的路径方法： get_topic()
        :param p1: 用户博文的开始页
        :param p2: 用户博文的结束页
        :param s: 信号量，用来控制get_topic中可能产生的变量冲突
        :return:
        """
        try:
            print '正在爬取用户', self.one_user, '相关信息,开始时间:', time.time()
            one = GetHunterWeibo(self.one_user).one_id_text(self.one_user, p1, p2)  # 字典{id:所有内容}
            print len(one.items())
            if len(one.items()) != 0:
                write_hunter_txt(self.hunter_text_dir,one.keys(), one.values())  # 写入方法
                # self.get_comment(one.keys(), one.values())
                # self.get_forward_path(one.keys(), one.values())

                all_topic = get_topic(one.keys(), one.values(), s)  # 三个列表元组 ,(话题, id, 博文)

                weibo_list = all_topic[2]
                weibo_keywords = []
                for one_weibo in weibo_list:
                    one_weibo_key = Keyword().combine_keywords(one_weibo)  # 博文的关键词提取
                    weibo_keywords.append(one_weibo_key)

                tp_and_wk = zip(all_topic[0], weibo_keywords, all_topic[1])  # [(话题,博文关键字,话题id)]，列表
                print "字典未增加检测事件的数量", len(WeiboPage.afore_all_uid)

                WeiboPage.afore_all_uid.setdefault(one.keys()[0], tp_and_wk)  # 用字典保存，这个猎头检测到的新事件,键是猎头，值是元组列表

                print "字典增加检测事件后的数量", len(WeiboPage.afore_all_uid)
                print WeiboPage.afore_all_uid.keys(), WeiboPage.afore_all_uid.values()
                get_topic_process = []
                for one_tuple in tp_and_wk:
                    get_topic_process = multiprocessing.Process(target=SearchTopic(self.one_user).get_search_topic, args=(one.keys(), one_tuple))
                    get_topic_process.start()
                get_topic_process.join()

            self.dictwt.clear()  # 清空一个用户的信息,准备开始下一个用户

        except AttributeError:
            print "get page error"


