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
import httplib2
reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'gu'


class WeiboPage():
    """
    父类
    定义了一些变量和一些公用方法
    """
    manager = Manager()
    all_all_topic = []  # 保存话题事件
    all_all_topic= manager.list() # 多进程共享变量
    afore_all_uid = {}  # 保存该话题的全部属性
    afore_all_uid = manager.dict()

    def __init__(self, one_user):
        """
        :param one_user: 用户的id，即是猎头的id
        :return:
        """
        self.one_user = one_user
        self.weibo_list = []
        self.time_list = []
        self.weibo = []
        self.writing_time = []
        self.base_page = []
        self.dictwt = {}
        self.no_repeat_list = []
        self.hunter_text_dir = os.path.join(BASE_DIR, 'documents', 'hunter_text/')
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
        extra1 = re.compile('</span>.*$')  # 匹配输入字符串的结束位置
        today = re.compile('今天')
        ago = re.compile('\d+分钟前')

        wbtime = re.sub(extra1, ' ', item1)
        t = time.strftime('%m' + '月' + '%d' + '日', time.localtime())
        t = t.decode('utf-8')
        wbtime = re.sub(today, t, wbtime)
        wbtime = re.sub(ago, t, wbtime)  # wbtime,gb2312,type str
        return wbtime

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

        blog_origin_patternts = re.compile('>(http://t.cn/.*?)</a></span>')
        blog_origin = blog_origin_patternts.findall(forward_page)

        if len(blog_origin) > 0:
            blog_origin = [re.sub(useless, '', blog_origin[0])]
            self.link = blog_origin[0]

        if len(blog_origin) == 0:
            blog_origin.append(str(None))

        forward_string_list = []
        for k in forward_path:
            k0 = re.sub(label_pattern, '', k[0])
            kk = re.sub(other_patterns, "", k[1])
            forward_reason1 = re.sub(label_pattern, "", kk)
            forward_reason2 = re.sub(link_pattern, '', forward_reason1)
            forward_reason = re.sub(space_pattern, '', forward_reason2)

            forward_string = str(k0) + ": " + str(forward_reason)
            forward_string_list.append(forward_string)
        # print "小去重前", len(forward_string_list)
        no_repeat_list = list(set(forward_string_list))
        no_repeat_list.sort(key=forward_string_list.index)
        # print "小去重后", len(no_repeat_list)
        return no_repeat_list, blog_origin  # 返回转发路径和博文源



