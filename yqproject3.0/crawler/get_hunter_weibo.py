# coding=utf-8
__author__ = 'gu'
"""
5.17检测完毕
"""
from class_weibo import *

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
            if (re.match('今天', tu[7])):  # tu[7]里找到标志为今天的时间
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

            elif (re.search('\d+分钟前', tu[7])):  # tu[7]里找到标志为几分钟前的时间
                if len(tu[7]) > 0:
                    self.dictwt.setdefault(tu[0], []).append(tu[1])
                    self.dictwt.setdefault(tu[0], []).append(tu[2])  # 键为tu[0],即是博文id,tu[1]没处理的博文
                    self.dictwt.setdefault(tu[0], []).append(tu[3])
                    self.dictwt.setdefault(tu[0], []).append(tu[4])  # tu[2]点赞数,tu[3]为转发链接,tu[4]为转发数量
                    self.dictwt.setdefault(tu[0], []).append(tu[5])
                    self.dictwt.setdefault(tu[0], []).append(tu[6])  # tu[5]是评论链接 tu[6]为评论数 tu[7]是时间
                    self.dictwt.setdefault(tu[0], []).append(tu[7])
                else:
                    pass
            else:
                print "这不是今天的博文"

        print 'len', len(self.dictwt)

        return self.dictwt

    def one_id_text(self, i, a, b):
        """
        爬取用户博文的方法
        :param i: 用户的id
        :param a: 博文的开始页
        :param b: 博文的结束页
        :return: 返回 all_dict ，键为今天发表了博文用户的id，值为这个id的博文,时间,赞,转发链接 转发,评论链接 评论 组成的元组列表
        """
        all_dict = {}
        writing_time = []
        weibo = []  # 存放一个人的所有博文
        weibo_id = []
        praise = []  # 赞
        forward = []  # 转发
        comment = []  # 评论
        forward_url = []
        comment_url = []
        blog_origin = []

        try:
            host_url = "http://weibo.cn/u/" + str(i)
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

                url = "http://weibo.cn/u/" + str(self.one_user) + "?page=" + str(k)  # 猎头的首页
                req = urllib2.Request(url=url, headers=self.header)
                self.homepage = urllib2.urlopen(req).read()

                base_patterns = re.compile(
                    'class="c" id="(.*?)">.*?<span class="ctt">(.*?)</span>.*?>赞\[(\d+)]</a>&nbsp;<a href="(.*?)">转发\[(\d+)]</a>&nbsp;<a href="(.*?)" class="cc">评论\[(\d+)]</a>.*?<span class="ct">(.*?)&nbsp',
                    re.M)  # 匹配博文id 、博文 点赞 转发链接 转发 评论链接 评论 时间
                self.base_page = base_patterns.findall(self.homepage)
                if len(self.base_page) > 0:
                    print "登陆成功"
                else:
                    print "登陆失败"
                self.add_text()

            for id in self.dictwt.keys():
                print id

            if len(self.dictwt) > 0:
                print "用户 ", i, "今天有发表博文"
                for item0, item1 in self.dictwt.items():  # item0为tu[0],键=博文id. item1 = 值

                    weibo_id.append(item0)  # 键=博文id
                    wbtime = self.cleaned_wbtime(item1[6])  # 清理博文时间

                    blog_origin_patternts = re.compile('>(http://t.cn/.*?)</a></span>')
                    blog_origin_one = blog_origin_patternts.findall(item1[0])  # 爬取新闻链接
                    if len(blog_origin_one) == 0:
                        blog_origin.append(str(None))
                    else:
                        blog_origin.append(blog_origin_one[0])

                    content = self.cleaned_weibo(item1[0])  # 清理博文

                    writing_time.append(wbtime)  # 存放时间
                    weibo.append(content)  # 存放博文
                    praise.append(item1[1])  # 点赞量
                    forward_url.append(item1[2])  # 转发量url
                    forward.append(item1[3])
                    comment_url.append(item1[4])  # 评论量url
                    comment.append(item1[5])

            else:
                print "用户", i, "今天没有发表博文"

            if len(weibo) > 0:
                # 各种列表打包
                tw = zip(writing_time, weibo_id, weibo, praise, forward_url, forward, comment_url, comment, blog_origin)
                all_dict.setdefault(i, tw)
        except:
            pass

        return all_dict  # 返回字典，键为有动态的id，值为这个id的博文,时间,赞,转发,评论,博文链接组成的元组列表
