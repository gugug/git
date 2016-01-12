# coding=utf-8
__author__ = 'gu'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import django, os
from class_login import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dbtest2.settings")
django.setup()

import time, random, urllib2, re, multiprocessing as mul, MySQLdb, cookielib, urllib, sys, chardet
from dua.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from _mysql_exceptions import ProgrammingError

from class_all_id import *
from class_mysql_uid import *


class Page(Uid):
    def __init__(self):
        Uid.__init__(self)
        self.weibo_list = []
        self.time_list = []
        self.weibo = []
        self.writing_time = []
        self.activity_list = []
        self.no_repeat_list = []
        self.all_dict = {}

    def getId(self, text):
        dict_text = eval(text)
        self.user_list = dict_text["user_id"]
        return self.user_list

    def download(self):
        # PostData = {'number':num}
        request = urllib2.Request(url='http://192.168.1.40:8000/get_id', headers=self.header)
        response = urllib2.urlopen(request)
        text = response.read()
        dict_text = eval(text)  # json转化为字典
        # print dict_text
        # print type(dict_text)
        self.user_list = dict_text["user_id"]
        # print type(user_lists)
        self.getPage(self.user_list, 1, 2)
        return self.user_list

    # 输入想要的用户博文页数,获取用户博文和时间并存入数据库
    def getPage(self, user_list, p1, p2):
        # print user_list
        print '正在储存博文和时间,开始时间:', time.time()
        for i in user_list:  # i=一个人的id
            print "第", user_list.index(i) + 1, "个人,id:", i
            one = self.one_id_text(i, p1, p2)  # 调用子函数,返回的是字典形式，键是id，值是用户博文和时间
            print "key", one.keys()
            print "value", one.values()


            print '活跃用户的个数', len(one.keys())

            # for j in xrange(len(one.keys()) - 1):
            #     one_time = one[0][j + 1]  # 单条时间,博文
            #     one_text = one[1][j + 1]
            #     # wt = (one_time,one_text)
            #     self.weibo_list.append(one_text)  # 以下三句用于写txt文件
            #     self.time_list.append(one_time)

            self.write_txt()  # 调用方法写入txt

            print '储存博文和时间完成'
        return True

    def one_id_text(self, i, a, b):  # 传入第i个用户的id,ab为开始和结束的页数,返回这个用户的博文
        writing_time = []
        weibo = []
        dict = {}
        # reload(sys)
        # sys.getdefaultencoding('utf8')
        self.sleep()
        host_url = "http://weibo.cn/u/" + str(i)
        url_request = urllib2.Request(host_url, headers=self.header)
        response = urllib2.urlopen(url_request)
        text = response.read()
        page_num = re.compile('跳页" />.*?/(.*?)页')  # 匹配微博页数
        num = page_num.findall(text)
        for nm in num:
            pm = int(nm)
            if b > pm:
                b = pm
            else:
                pass
        for k in xrange(a, b):
            if k % 5 == 4:  # change here
                self.sleep()
            else:
                pass
            print "第", k, "页"
            zyurl = "http://weibo.cn/u/" + str(i) + "?page=" + str(k)
            req = urllib2.Request(url=zyurl, headers=self.header)
            # self.sleep()
            zytext = urllib2.urlopen(req).read()
            zytext = str(zytext).decode('utf-8')
            # print zytext
            psg = re.compile('</span><span class="ctt">(.*?)</span>.*?<span class="ct">(.*?)&nbsp', re.M)  # 匹配用户的正文和时间

            # agopsg = re.compile('"ctt">(.*?)</span>.*?<span class="ct">(.分钟前)&nbsp', re.M)  # 匹配标志有几分钟前的正文和时间
            passage = psg.findall(zytext)  # 一个用户今天的所有博文
            # passage1 = agopsg.findall(zytext)  #  一个用户几分钟前的所有博文(一个小时前)

            if (len(passage) == 0):
                print '该账号无法使用'
                self.sleep()
                k -= 1
            else:
                print "帐号登录正常"

                for tu in passage:
                    if (re.match(U'\d分钟前', tu[1])):  # tu[1]里找到标志为今天的时间
                        if len(tu[1]) > 0:
                            print "这条博文是今天发表的", tu[1]
                            dict.setdefault(tu[0], tu[1])
                        else:
                            pass

                    elif (re.search(U'今天', tu[1])):  # tu[1]里找到标志为几分钟前的时间
                        if len(tu[1]) > 0:
                            print "这条博文是几分钟前发表的"
                            dict.setdefault(tu[0], tu[1])  # 键为tu[0],即是博文,值为tu[1],即是时间
                        else:
                            pass

                    else:
                        print "这不是今天的博文"

                for item0, item1 in dict.items():  # item0为tu[0],博文.  item1为tu[1],时间
                    # print "item0",item0
                    # print "item1",item1
                    extra1 = re.compile('</span>.*$')  # 匹配输入字符串的结束位置
                    # extra2=re.compile('</span>.*?</a>')
                    today = re.compile(u'今天')
                    ago = re.compile(u'\d分钟前')
                    wbtime = re.sub(extra1, ' ', item1)  # 在item1中把extra1都用空格替换掉

                    t = time.strftime('%m' + '月' + '%d' + '日', time.localtime())
                    t = t.decode('utf-8')

                    wbtime = re.sub(today, t, wbtime)
                    wbtime = re.sub(ago, t, wbtime)

                    writing_time.append(wbtime)

                    # print "第",passage.index(tu)+1,"篇博文,发表时间",time
                    # content=tu[0].encode('gbk','ignore') #gbk就是字符串
                    sub_title = re.compile(u'<img.*?注')
                    tag = re.compile('</a>')  # 去除标签
                    link = re.compile('<a href=.*?>|http.*?</a>')  # 去除链接
                    content = re.sub(link, " ", item0)
                    content = re.sub(tag, '', content)
                    content = re.sub(sub_title, '', content)
                    content = content.encode('utf-8', 'ignore')
                    weibo.append(content)
                    # if len(weibo) > 0:

                    # print "这是今天有动态的用户",i
                    self.activity_list.append(i)
                    self.no_repeat_list = list(set(self.activity_list))  # 去重，把重复的id去除
                    self.no_repeat_list.sort(key=self.activity_list.index)

                    # print "活跃用户的列表及长度",len(self.no_repeat_list),self.no_repeat_list

                tw = zip(writing_time, weibo)  # 用元组绑定每条的时间和博文
                print "活跃用户的列表及长度", len(self.no_repeat_list), self.no_repeat_list

                for key_id in self.no_repeat_list:
                    self.all_dict.setdefault(key_id, tw)  # id作为键，时间博文绑定后作为值
        return self.all_dict

    # 与getPage联合发动,写入txt,可禁用或开启
    def write_txt(self):  # 一个人的id和他的时间,微博列表

        print '正在写入博文'
        for key, value in self.all_dict.items():
            file = open(self.text_dir + 'uid=' + str(key) + '.txt', 'w+')

            for i in value:
                print "key", key
                print "i[0],[1]", i[0], i[1]

                # 写入数据库
                # try:
                #     WeiboText.objects.get(user_id=key, time=i[0], weibo=i[1])
                # except ObjectDoesNotExist:
                #         try:
                #             WeiboText.objects.create(user_id=key, time=i[0], weibo=i[1])
                #         except ProgrammingError:
                #             print '博文无法存入数据库'
                #             continue

                file.write(key + ',' + i[0] + ',' + i[1] + '\n')
            file.close()
        print '完成输入博文'

        #
        # zipper = zip(time_list, weibo_list)
        # print '正在写入博文'
        # print "活跃用户的个数",len(self.activity_list)
        # for no_repeat_item in self.no_repeat_list:
        #     for item in self.activity_list:
        #         print "item"+item
        #
        #         if no_repeat_item == item:
        #         # if len(self.activity_list) is not None:
        #         #     not_number = re.compile('\D')
        #         #     uid = re.sub(not_number, '', str(item))
        #             file = open(self.text_dir + 'uid=' + str(item) + '.txt', 'w+')
        #         # else:
        #             # file = open(self.text_dir + self.default_title + '.txt', 'w+')
        #
        #         for i in zipper:
        #             time = i[0]
        #             weibo = i[1]
        #             print time
        #             print type(weibo)
        #             print item
        #             time = time.encode('utf-8', 'ignore')
        #             weibo = weibo.decode('utf-8')
        #             # weibo = weibo.encode('utf-8','ignore')
        #             # print type(time),type(weibo),type(uid)
        #             file.write(item + ',' + time + ',' + weibo + '\n')
        #             file.close()
        #     print '完成输入博文'

# """
# 测试
# """
#
# import os
# import django
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dbtest2.settings")
# django.setup()
l = Login()
l.login("18826103742", "183182")

db = Database()  # ip连接数据库,取出数据库的方法
uid = db.get_mysql_user(1, 20)  # 取出具体区域的id
# # print uid

page_crawler = Page()
# page_crawler.one_id_text(1742566624,1,3)
page_crawler.getPage(uid, 1, 2)  # 把取出的id传入参数，进行爬博文1920061532
