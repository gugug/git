# coding=utf-8
"""
5.16
程序基本可以运行，除了那个存数据的很迷外。
实现了更新和检测
"""
import sys
from time import sleep
from crawl_headhunter import *
from create_file import *
from crawler.class_save_data import *
from get_keyword.get_keyword import *
from crawler.class_content import *
from crawler.class_event import *
from multiprocessing import Process, Manager
import os
import multiprocessing

reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'gu'

class WeiboPage:
    """
    父类
    定义了一些变量和一些公用方法
    """
    manager = Manager()
    # exist_topic = []
    # exist_topic = manager.list()  # 多进程共享变量, 保存话题事件
    #
    # searched_tpdict = {}
    # searched_tpdict = manager.dict()  # 保存该话题的全部属性(关键词,话题,博文id)

    detected_tpdict = {}
    detected_tpdict = manager.dict()

    all_hunterlist =[]
    all_hunterlist = manager.list()  # 保存猎头的全部博文,点赞之类的

    def __init__(self):
        """
        :param one_user: 用户的id，即是猎头的id
        :return:
        """
        self.weibo_list = []
        self.time_list = []
        self.weibo = []
        self.writing_time = []
        self.base_page = []
        self.dictwt = {}
        self.no_repeat_list = []
        self.comment_dir = os.path.join(BASE_DIR, 'documents', 'comment/')  # 猎头微博的评论内容
        self.forward_path_dir = os.path.join(BASE_DIR, 'documents', 'forward_path/')  # 猎头的微博的转发路径
        self.header = {'User-Agent': 'Mozilla/' + str(
            float(int(random.uniform(1, 6)))) + '(X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/' + str(
            float(int(random.uniform(29, 36))))}

        self.blog_id = ''
        self.post_time = ''
        self.event_id = ''
        self.corpus_dir = ''
        self.link = ''

    def cleaned_wbtime(self, item1):
        """
        转化时间格式
        :param item1: 时间
        :return:标准格式的时间 h:m:s
        """
        extra = re.compile('</span>.*$')  # 匹配输入字符串的结束位置
        today = re.compile('今天')
        ago = re.compile('\d+分钟前')

        post_time = re.sub(extra, '', item1)
        t = time.strftime('%m' + '月' + '%d' + '日', time.localtime())
        t = t.decode('utf-8')
        post_time = re.sub(today, t, post_time)
        post_time = re.sub(ago, t, post_time)
        return post_time

    def cleaned_weibo(self, item0):
        """
        净化博文
        :param item0:博文
        :return:净化干净的博文
        """
        sub_title = re.compile('<img.*?注')
        tag = re.compile('<.*?>')  # 去除标签
        link = re.compile('<a href=.*?>|http.*?</a>')  # 去除链接
        content = re.sub(link, "", item0)
        content = re.sub(tag, '', content)
        content = re.sub(sub_title, '', content)
        # content = content.encode('utf-8', 'ignore')  # content为完成的博文
        return content

    def get_forward_common(self, forward_url):
        """
        匹配转发路径及理由，用列表返回
        :param forward_url: 转发页的链接
        :return:该页的转发路径及理由
        """
        # 转发页需要用到的正则
        forward_patterns = re.compile(
            # '<div class="s"></div><div class="c"><a href="/u/(.*?)">(.*?)</a>.*?:(.*?)&nbsp'   # 匹配全部转发者
            '//<a href="/n.*?>(@.*?)</a>:(.*?)&nbsp;')  # 去除最后一个转发者的路径
        other_patterns = re.compile('//<.*?>')
        label_pattern = re.compile('<.*?>')
        useless = re.compile('</a>.*$')
        link_pattern = re.compile('<a href=.*?>|http.*?</a>')  # 去除链接
        space_pattern = re.compile('&nbsp;')

        req = urllib2.Request(url=forward_url, headers=self.header)
        forward_page = urllib2.urlopen(req).read()
        time.sleep(int(random.uniform(0, 2)))

        forward_path = forward_patterns.findall(forward_page)

        blog_origin_pattern = re.compile('>(http://t.cn/.*?)</a></span>')
        blog_origin = blog_origin_pattern.findall(forward_page)

        if len(blog_origin) > 0:
            blog_origin = [re.sub(useless, '', blog_origin[0])]
            self.link = blog_origin[0]
        else:
            blog_origin.append(str(None))

        forward_string_list = []
        for k in forward_path:
            k0 = re.sub(label_pattern, '', k[0])
            kk = re.sub(other_patterns, '', k[1])
            forward_reason1 = re.sub(label_pattern, '', kk)
            forward_reason2 = re.sub(link_pattern, '', forward_reason1)
            forward_reason = re.sub(space_pattern, '', forward_reason2)

            forward_string = str(k0) + ": " + str(forward_reason)
            forward_string_list.append(forward_string)
        no_repeat_list = list(set(forward_string_list))
        no_repeat_list.sort(key=forward_string_list.index)
        return no_repeat_list, blog_origin  # 返回转发路径和博文源

        # def match_topic(self,list_key, tuple_value, s):
        #     """
        #     爬取博文的主题，【】内的内容
        #     :param key:list 猎头的id [201783423]
        #     :param value: 值为(时间,博文,点赞,转发链接,转发量,评论链接,评论量）元组组成的列表
        #     :param s： 信号量 控制进程中变量的冲突
        #     :return: weibo_topic, blog_id_list, weibo (tuple)  三个列表的元组， 返回还没有被检测的话题事件
        #     weibo_topic (list) 表示当前检测到的新话题事件
        #     blog_id_list (list) 表示当前博文的id
        #     weibo (list) 表示博文
        #     """
        #
        #     weibo_topic = []
        #     blog_id_list = []
        #     weibo = []
        #     print "检测前保存的话题数量为", len(WeiboPage.exist_topic)
        #     for i in tuple_value:
        #         for j in i:
        #             topic_patternts = re.compile('#(.*?)# |【(.*?)】')
        #             topic = topic_patternts.findall(j[2])
        #             if len(topic) > 0:
        #                 topic = topic[0][0] + topic[0][1]
        #                 topic_clean_pattern = re.compile('(\[.*?])')
        #                 topic = re.sub(topic_clean_pattern, '', topic)
        #                 topic_clean2_pattern = re.compile('#(.*?)#')
        #                 topic = [re.sub(topic_clean2_pattern, '', topic)]
        #
        #                 s.acquire()  # 信号量控制
        #                 if topic[0] not in WeiboPage.exist_topic:  # 对已搜索过的话题进行去除
        #                     WeiboPage.exist_topic.append(topic[0])  # 专门保存话题的变量中增加新检测到的话题
        #                     weibo_topic.append(topic[0])  # 保存只在这次检测过程中发现的话题
        #                     blog_id_list.append(j[1])  # 保存每个新事件的bid
        #                     weibo.append(j[2])  # 保存发现新事件的原文博文
        #                 else:
        #                     print "该话题不属于新检测到的事件", topic[0]
        #                 s.release()
        #             else:
        #                 print "这篇博文没有话题，检测不到事件"
        #
        #     print "检测到的新事件数量", len(weibo_topic)
        #
        #     for ntopic in weibo_topic:
        #         print list_key,"检测到的新事件", ntopic
        #
        #     print "保存到的话题最新数量", len(WeiboPage.exist_topic)
        #     for stopic in WeiboPage.exist_topic:
        #         print "保存的话题有：", stopic
        #     return weibo_topic, blog_id_list, weibo
