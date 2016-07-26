# coding=utf-8
from write_hunter_txt import *

from crawl_weibo import *

__author__ = 'gu'
"""
5.28 测试完毕
"""


class GetHunterWeibo(WeiboPage):
    """
    爬取微博用户的当天的博文，用于后面的处理，这个微博用户是我们自己准备的猎头
    """

    def add_text(self):
        """
            判断爬取的博文是否为今天发表的，如果是则保存在字典里
            :return:  self.dictwt 键为博文，值为博文相关的属性 （匹配博文id 、博文 点赞 转发链接 转发 评论链接 评论 时间）

            键为tu[0],即是博文id,tu[1]为没处理的博文
            tu[2]点赞数,tu[3]为转发链接,tu[4]为转发数量
            tu[5]是评论链接 tu[6]为评论数 tu[7]是时间
        """
        for tu in self.base_page:  # tu:每一条博文块
            if (re.match('今天', tu[7])):
                if len(tu[7]) > 0:
                    self.dictwt.setdefault(tu[0], []).append(tu[1])
                    self.dictwt.setdefault(tu[0], []).append(tu[2])
                    self.dictwt.setdefault(tu[0], []).append(tu[3])
                    self.dictwt.setdefault(tu[0], []).append(tu[4])
                    self.dictwt.setdefault(tu[0], []).append(tu[5])
                    self.dictwt.setdefault(tu[0], []).append(tu[6])
                    self.dictwt.setdefault(tu[0], []).append(tu[7])
                else:
                    pass
            elif (re.search('\d+分钟前', tu[7])):
                if len(tu[7]) > 0:
                    self.dictwt.setdefault(tu[0], []).append(tu[1])
                    self.dictwt.setdefault(tu[0], []).append(tu[2])
                    self.dictwt.setdefault(tu[0], []).append(tu[3])
                    self.dictwt.setdefault(tu[0], []).append(tu[4])
                    self.dictwt.setdefault(tu[0], []).append(tu[5])
                    self.dictwt.setdefault(tu[0], []).append(tu[6])
                    self.dictwt.setdefault(tu[0], []).append(tu[7])
                else:
                    pass
            else:
                print "这不是今天的博文"
        print "长度", len(self.dictwt)
        return self.dictwt

    def one_id_text(self, one_user, a, b, s):
        """
            爬取猎头博文的方法
            :param a: 博文的开始页
            :param b: 博文的结束页
            :param s: 信号量，防止多进程时，WeiboPage.all_hunterlist, append时冲突
            :return: all_dict  字典的键，即是uid, 值为(时间,博文id,博文,点赞,转发链接,转发量,评论链接,评论量,新闻源）元组组成的列表

        """
        all_dict = {}
        writing_time = []
        weibo = []
        weibo_id = []
        praise = []
        forward = []
        comment = []
        forward_url = []
        comment_url = []
        blog_origin = []

        try:
            host_url = "http://weibo.cn/u/" + str(one_user)
            url_request = urllib2.Request(host_url, headers=self.header)
            response = urllib2.urlopen(url_request, timeout=30)
            text = response.read()
            page_num = re.compile('跳页" />.*?/(.*?)页')  # 匹配微博页数
            num = page_num.findall(text)

            for nm in num:  # 判断页数,不足b页时到pm页为止
                pm = int(nm)
                if b > pm:
                    b = pm
                else:
                    pass

            for k in xrange(a, b):  # 每一页的博文获取
                if k % 5 == 4:
                    time.sleep(random.randint(0, 5))
                else:
                    pass
                print "第", k, "页"

                url = "http://weibo.cn/u/" + str(one_user) + "?page=" + str(k)  # 猎头的首页
                req = urllib2.Request(url=url, headers=self.header)
                homepage = urllib2.urlopen(req).read()
                # print homepage

                base_patterns = re.compile(
                    'class="c" id="(.*?)">.*?<span class="ctt">(.*?)</span>.*?>赞\[(\d+)]</a>&nbsp;<a href="(.*?)">转发\[(\d+)]</a>&nbsp;<a href="(.*?)" class="cc">评论\[(\d+)]</a>.*?<span class="ct">(.*?)&nbsp',
                    re.M)  # 匹配博文id 、博文 点赞 转发链接 转发 评论链接 评论 时间
                self.base_page = base_patterns.findall(homepage)
                if len(self.base_page) > 0:
                    print "登陆成功"
                else:
                    print "登陆失败"
                self.add_text()  # 进行今天的博文筛选

            if len(self.dictwt) > 0:
                print "用户 ", one_user, " 今天有发表博文"
                for item0, item1 in self.dictwt.items():  # item0为tu[0],键=博文id. item1 = 值

                    weibo_id.append(item0)
                    post_time = self.cleaned_wbtime(item1[6])

                    blog_origin_patternts = re.compile('>(http://t.cn/.*?)</a></span>')
                    blog_origin_one = blog_origin_patternts.findall(item1[0])
                    if len(blog_origin_one) == 0:
                        blog_origin.append(str(None))
                    else:
                        blog_origin.append(blog_origin_one[0])

                    content = self.cleaned_weibo(item1[0])

                    writing_time.append(post_time)
                    weibo.append(content)
                    praise.append(item1[1])
                    forward_url.append(item1[2])
                    forward.append(item1[3])
                    comment_url.append(item1[4])
                    comment.append(item1[5])

            else:
                print "用户 ", one_user, " 今天没有发表博文"

            if len(weibo) > 0:
                all_list = zip(writing_time, weibo_id, weibo, praise, forward_url, forward, comment_url, comment,
                               blog_origin)
                all_dict.setdefault(one_user, all_list)

                s.acquire()
                WeiboPage.all_hunterlist.append(all_dict)  # 中间变量保存全部猎头的博文
                s.release()

                self.dictwt.clear()  # 清空一个用户的信息,准备开始下一个用户

        except:
            pass

        write_hunter_txt(all_dict.keys(), all_dict.values())
        return all_dict


