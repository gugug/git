# coding=utf-8
__author__ = 'yc'

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import django, os
from ProxyIP.proxyIp import *
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dbtest2.settings")
django.setup()
from class_mysql_uid import *
from class_all_id import *


class Page(Uid):
    def __init__(self):
        Uid.__init__(self)
        self.weibo_list = []
        self.time_list = []
        self.weibo = []
        self.writing_time = []
        # self.activity_list = []
        # self.no_repeat_list = []
        # self.all_dict = {}

    def count(self, uid, i):  # uid为所有人的列表
        number = uid.index(i) + 1
        print "第", number, "个人"

    # 输入想要的用户博文页数,获取用户博文和时间并存入数据库
    def getPage(self, one_user, p1, p2):  # one_user:1个用户,p1,p2:页数
        print '正在储存博文和时间,开始时间:', time.time()
        print "id:", one_user
        one = self.one_id_text(one_user, p1, p2)  # 调用子函数,one_text本身是列表,形式([time],[weibo])
        # writng_text 插入处
        self.write_txt(one.keys(), one.values())
        print '储存', one_user, '博文和时间完成'
        return True

    def one_id_text(self, i, a, b):  # i:一个用户的id,ab为开始和结束的页数,返回这个用户的博文
        activity_list = []
        no_repeat_list = []
        all_dict = {}
        writing_time = []
        weibo = []  # 存放一个人的所有博文
        dictwt = {}
        self.sleep()  # 切换账号
        host_url = "http://weibo.cn/u/" + str(i)
        setIpProxy(getIpInFile())
        url_request = urllib2.Request(host_url, headers=self.header)
        response = urllib2.urlopen(url_request)
        text = response.read()
        page_num = re.compile('跳页" />.*?/(.*?)页')  # 匹配微博页数
        num = page_num.findall(text)

        for nm in num:  # 判断页数,不足b页时到pm页为止
            pm = int(nm)
            if b > pm:
                b = pm
                print "b", b
            else:
                pass

        for k in xrange(a, b):  # 每一页的博文获取
            print "kk"
            if k % 5 == 4:
                time.sleep(random.randint(0, 5))
            elif k % 7 == 6:
                self.sleep()
            else:
                pass
            print "第", k, "页"
            zyurl = "http://weibo.cn/u/" + str(i) + "?page=" + str(k)
            setIpProxy(getIpInFile())
            req = urllib2.Request(url=zyurl, headers=self.header)
            # self.sleep()
            zytext = urllib2.urlopen(req).read()
            zytext = str(zytext).decode('utf-8')
            psg = re.compile('<span class="ctt">(.*?)</span>.*?<span class="ct">(.*?)&nbsp', re.M)  # 匹配时间和博文
            passage = psg.findall(zytext)  # 一个用户所有的博文和时间
            if (len(passage) == 0):
                print '该账号无法使用'
                self.sleep()
                k -= 1
            else:
                print "帐号正常"

                for tu in passage:  # tu:每一条博文块
                    # 判断是否今天博文
                    if (re.match(U'今天', tu[1])):  # tu[1]里找到标志为今天的时间
                        if len(tu[1]) > 0:
                            # print "这是今天的博文"
                            dictwt.setdefault(tu[0], tu[1])
                        else:
                            pass

                    elif (re.search(U'\d分钟前', tu[1])):  # tu[1]里找到标志为几分钟前的时间
                        if len(tu[1]) > 0:
                            # print "这是今天的博文"
                            dictwt.setdefault(tu[0], tu[1])  # 键为tu[0],即是博文,值为tu[1],即是时间
                        else:
                            pass
                    else:
                        print "这不是今天的博文"
                        pass
                # 去除博文和时间里的标签
                if len(dictwt) > 0:
                    print "用户 ", i, "今天有发表博文"
                    activity_list.append(i)  # 把有动态的用户添加到列表,反动一页就存放一次
                    no_repeat_list = list(set(activity_list))    # 去重，把重复的id去除
                    no_repeat_list.sort(key=activity_list.index)
                    # print "活跃用户的列表及长度",len(self.no_repeat_list),self.no_repeat_list
                    for item0, item1 in dictwt.items():  # item0为tu[0],博文.  item1为tu[1],时间
                        extra1 = re.compile('</span>.*$')  # 匹配输入字符串的结束位置
                        today = re.compile(u'今天')
                        ago = re.compile(u'\d+分钟前')
                        wbtime = re.sub(extra1, ' ', item1)  #
                        t = time.strftime('%m' + '月' + '%d' + '日', time.localtime())
                        t = t.decode('utf-8')
                        wbtime = re.sub(today, t, wbtime)
                        wbtime = re.sub(ago, t, wbtime)  # wbtime,gb2312,type str
                        writing_time.append(wbtime)      # 存放时间

                        sub_title = re.compile(u'<img.*?注')
                        tag = re.compile('</a>')  # 去除标签
                        link = re.compile('<a href=.*?>|http.*?</a>')  # 去除链接
                        content = re.sub(link, " ", item0)
                        content = re.sub(tag, '', content)
                        content = re.sub(sub_title, '', content)
                        content = content.encode('utf-8', 'ignore')  # content为去噪完成的博文
                        weibo.append(content)                        # 存放博文
                        # print weibo
                        # print writing_time
                else:
                    print "用户", i, "今天没有发表博文"
                if len(weibo) > 0:
                    tw = zip(writing_time, weibo)  # 用元组绑定每条的时间和博文
                    print writing_time
                    print weibo
                    all_dict.setdefault(i, tw)
                else:
                    pass

        return all_dict  # 返回字典，键为有动态的id，值为这个id的博文和时间组成的元组列表

    # 写博文txt备份,在getPage中启动或禁用
    def write_txt(self, key, value):  # 一个人的id和他的时间,微博列表
        print '正在写入博文'
        for i in value:
            print key[0], "今天发的博文数量", len(i)
            file = open(self.text_dir + 'uid=' + str(key[0]) + '.txt', 'w+')
            print "创建文件成功"
            for j in i:
                print "key,i[0],[1]", key[0], j[0], j[1]
                file.write(str(key[0]) + ',' + str(j[0]) + ',' + str(j[1]) + '\n')

                # 写入数据库
                # try:
                #     WeiboText.objects.get(user_id=key[0], time=j[0], weibo=j[1])
                # except ObjectDoesNotExist:
                #         try:
                #             WeiboText.objects.create(user_id=key[0], time=j[0], weibo=j[1])
                #         except ProgrammingError:
                #             print '博文无法存入数据库'
                #             continue
            file.close()
        print '完成输入博文'

