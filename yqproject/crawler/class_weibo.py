# coding=utf-8
"""
5.7:
更新了新需求，处理了检测的猎头为随机的5个 main_weibo()
并且程序是先更新在检测新事件 get_page()
"""
import sys
from class_headhunter import *
from create_file import *
from crawler.class_save_data import *
from get_keyword.get_keyword import *
from crawler.class_content import *
from crawler.class_event import *
reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'gu'


class WeiboPage():
    """
    本类爬取新浪微博用户的博文及评论
    """

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
        self.all_all_topic = []
        self.afore_all_uid = {}
        self.blog_id =''
        self.post_time = ''
        self.event_id = ''
        self.corpus_dir = ''
        self.link = ''


    # 把爬取到的内容加入字典
    def add_text(self):
        """
        判断爬取的博文是否为今天发表的，如果是则保存在字典里
        :return:  self.dictwt 键为博文，值为博文相关的属性
        """
        # 匹配博文id 、博文 点赞 转发链接 转发 评论链接 评论 时间
        for tu in self.base_page:  # tu:每一条博文块
            # 判断是否今天博文
            if (re.match('今天', tu[7])):  # tu[7]里找到标志为今天的时间
                if len(tu[7]) > 0:
                    self.dictwt.setdefault(tu[0], []).append(tu[1])
                    self.dictwt.setdefault(tu[0], []).append(tu[2])  # 键为tu[0],即是博文id,tu[1]为没处理的博文
                    self.dictwt.setdefault(tu[0], []).append(tu[3])
                    self.dictwt.setdefault(tu[0], []).append(tu[4])  # tu[2]点赞数,tu[3]为转发链接,tu[4]为转发数量
                    self.dictwt.setdefault(tu[0], []).append(tu[5])
                    self.dictwt.setdefault(tu[0], []).append(tu[6])  # tu[5]是评论链接 tu[6]为评论数 tu[7]是时间
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
        weibo = []       # 存放一个人的所有博文
        weibo_id = []
        praise = []      # 赞
        forward = []     # 转发
        comment = []     # 评论
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

                    writing_time.append(wbtime)             # 存放时间
                    weibo.append(content)                   # 存放博文
                    praise.append(item1[1])                 # 点赞量
                    forward_url.append(item1[2])            # 转发量url
                    forward.append(item1[3])
                    comment_url.append(item1[4])            # 评论量url
                    comment.append(item1[5])

                    print "博文id", item0
                    print "博文", item1[0]
                    print "点赞", item1[1]
                    print "转发", item1[3]
                    print "评论", item1[5]
                    print '转发链接', item1[2]
                    print '评论链接', item1[4]

            else:
                print "用户", i, "今天没有发表博文"

            if len(weibo) > 0:
                # 各种列表打包
                tw = zip(writing_time, weibo_id, weibo, praise, forward_url, forward, comment_url, comment, blog_origin)
                all_dict.setdefault(i, tw)
        except :
            pass

        return all_dict  # 返回字典，键为有动态的id，值为这个id的博文,时间,赞,转发,评论,博文链接组成的元组列表

    def write_hunter_txt(self, key, value):
        """
        写猎头的博文txt备份,在get_page()中启动或禁用
        :param key: 字典的键，即是id
        :param value: 值为(时间,博文,点赞,转发链接,转发量,评论链接,评论量）元组组成的列表
        :return:
        """
        print '正在写入用户', key, '博文'
        for i in value:
            print "value", value
            print key[0], "今天发的博文数量", len(i)
            if os.path.exists(self.hunter_text_dir):
                pass
            else:
                os.mkdir(self.hunter_text_dir)
            save_file = open(self.hunter_text_dir + 'uid=' + str(key[0]) + '.txt', 'w+')
            print "创建文件成功"
            for j in i:
                print "id,时间,博文id,博文,点赞,转发链接,转发量,评论链接,评论量,新闻源", key[0], j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], \
                    j[8]
                save_file.write(
                    str(key[0])
                    + "\n博文id: " + str(j[0])
                    + "\n时间： " + str(j[1])
                    + "\n博文： " + str(j[2])
                    + "\n点赞量： " + str(j[3])
                    + "\n转发链接： " + str(j[4])
                    + "\n转发量： " + str(j[5])
                    + "\n评论链接 ： " + str(j[6])
                    + "\n评论量： " + str(j[7])
                    + "\n新闻源： " + str(j[8])
                    + '\n\n')
            save_file.close()
        print '完成用户', key, '的博文存储'

    def get_page(self, p1, p2):
        """
        调用全部方法，相当于控制器

        爬取博文的方法 one_id_text()
        保存猎头当天发表的博文和博转评方法：write_text()
        爬取猎头微博的评论内容： get_comment()
        爬取猎头的微博的转发路径方法： get_forward_path()
        搜索话题爬取话题相关微博的路径方法： get_topic()

        先更新后检测
        :param p1: 用户博文的开始页
        :param p2: 用户博文的结束页
        :return:
        """

        try:
            # 先更新
            if self.all_all_topic:  # 之前检测到的话题存在
                for uid, afore_tuple_list in self.afore_all_uid.items():
                    for afore_tuple in afore_tuple_list:
                        self.get_search_topic(uid, afore_tuple)  # 更新之前的猎头检测到的事件
                print "更新完毕，开始检测其他事件"

            # 更新完毕，开始检测
            print '正在爬取用户', self.one_user, '相关信息,开始时间:', time.time()
            one = self.one_id_text(self.one_user, p1, p2)  # 字典{id:所有内容}
            print "进入下一阶段"
            print len(one.items())
            if len(one.items()) != 0:
                self.write_hunter_txt(one.keys(), one.values())
                # self.get_comment(one.keys(), one.values())
                # self.get_forward_path(one.keys(), one.values())
                all_topic = self.get_topic(one.keys(), one.values())  # 三个列表元组 ,(话题, id, 博文)

                weibo_list = all_topic[2]
                weibo_keywords = []
                for one_weibo in weibo_list:
                    one_weibo_key = Keyword().combine_keywords(one_weibo)  # 博文的关键词提取
                    weibo_keywords.append(one_weibo_key)

                tp_and_wk=zip(all_topic[0], weibo_keywords, all_topic[1])  # [(话题,博文关键字,话题id)]，列表

                self.afore_all_uid.setdefault(one.keys()[0], tp_and_wk)  # 用字典保存，这个猎头检测到的新事件,键是猎头，值是元组列表

                for one_tuple in tp_and_wk:
                    a = multiprocessing.Process(target=self.get_search_topic, args=(one.keys(), one_tuple))
                    a.start()
                a.join()

            self.dictwt.clear()  # 清空一个用户的信息,准备开始下一个用户
        except AttributeError:
            print "get page error"
        return True

    def get_topic(self, key, value):
        """
        爬取博文的主题，【】内的内容
        :param key:
        :param value:
        :return: self.weibo_topic (list)全部话题
        """
        weibo_topic = []
        blog_id_list = []
        weibo = []
        for i in value:
            for j in i:
                print "id,时间,博文id,博文,点赞,转发链接,转发量,评论链接,评论量,新闻源", key[0], j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8]

                topic_patternts = re.compile('#(.*?)# |【(.*?)】')
                topic = topic_patternts.findall(j[2])

                if len(topic) > 0:

                    topic = [topic[0][0]+topic[0][1]]

                    topic_clean_pattern = re.compile('(\[.*?])')
                    topic = [re.sub(topic_clean_pattern, '', topic[0])]

                    if topic[0] not in self.all_all_topic:  # 对已搜索过的话题进行去除
                        weibo_topic.append(topic[0])
                        blog_id_list.append(j[1])
                        weibo.append(j[2])
                    else:
                        print "该话题已经搜索完毕，不再进行搜索", topic[0]
                else:
                    print "这篇博文没有话题，无法搜索"

        self.all_all_topic = list(set(self.all_all_topic + weibo_topic))  # 全局变量,保存全部话题,为下一个猎头话题去重

        print 'weibo长度',len(weibo_topic)
        print 'weibo_id长度',len(blog_id_list)
        print "weibochangdu",len(weibo)
        for tp in weibo_topic:
            print "话题有：", tp
        return weibo_topic, blog_id_list, weibo  # 三个列表的元组， 返回还没有被检测的话题事件

    def get_search_topic(self, uid, tuple):
        """
        此方法用来判断话题是否为热点
        :param topic: 要搜索的话题。str
        :return: 布尔值，是热点就返回true,不是热点就返回false
        """

        zhuti = tuple[0]  # 话题
        topic = tuple[1]  # 微博关键字
        blog_id = tuple[2]  # 话题id

        print tuple
        print "正在搜索话题关键词: ", topic
        hot_url = 'http://weibo.cn/search/mblog/?keyword=' + str(
            urllib2.quote(topic)) + '&sort=hot'
        print 'hot', hot_url
        req = urllib2.Request(url=hot_url, headers=self.header)
        result_page = urllib2.urlopen(req).read()
        print "result", result_page

        if "抱歉，未找到" in result_page:
            req = urllib2.Request(url=hot_url, headers=self.header)
            result_page = urllib2.urlopen(req).read()
            if "抱歉，未找到" in result_page:
                print "看来真的没有结果了~~~"
                return False

        if "抱歉，未找到" not in result_page:
            result_num_patternts = re.compile('<span class="cmt">共(.*?)条</span>')
            result_num = result_num_patternts.findall(result_page)
            if not result_num:
                result_num.append(1)
            print "result_num", result_num[0]

            if int(result_num[0]) > 1000:
                page_num = 10  # ps
            elif int(result_num[0]) <= 10:
                page_num = 0
            else:
                if int(result_num[0]) % 10 > 0:
                    page_num = int(result_num[0]) / 10 + 1
                else:
                    page_num = int(result_num[0]) / 10

            if page_num > 0:
                check = Event().check_topic(zhuti)
                print 'checking topic',check
                if check == True:
                    self.event_id = 'topic'+blog_id
                else:
                    self.event_id = check
                print "self.event_id+blog_id",self.event_id
                self.topic = zhuti
                Event().save_event_id(self.event_id)
                Database().save_participate(self.one_user, self.event_id)
                self.fold_dir = get_fold_path(zhuti)
                self.dynamic_dir = create_time_file(zhuti)  # 动态生成话题文件夹，全局变量
                print "生成的动态目录：", self.dynamic_dir
                corpus_dir = self.fold_dir + 'uid=' + str(uid) + '.txt'
                label_dir = self.fold_dir + 'new_label_link.xls'
                txt_file = open(corpus_dir, 'w+')

                big_v_num = 0
                print "有", result_num[0], "条结果,判断为热点新闻"
                like_all_num = 0
                forward_all_num = 0
                comment_all_num = 0
                for page in xrange(0, page_num):
                    page = int(page) + 1
                    pageurl = 'http://weibo.cn/search/mblog?keyword=' + str(
                        urllib2.quote(topic)) + '&sort=hot&page=' + str(page)
                    print pageurl

                    req = urllib2.Request(url=pageurl, headers=self.header)
                    result_turn_page = urllib2.urlopen(req).read()
                    issuer_patternts = re.compile('<div class="c" (id.*?)<div class="s"></div>')  # 把每个人的一个整个匹配下来
                    issuer = issuer_patternts.findall(result_turn_page)
                    for item in issuer:
                        if 'alt="V"/>' in item:
                            big_v_num += 1  # 记录大v的个数

                            issuer_all_patternts = re.compile(
                                'class="c" id="(.*?)">.*?<span class="ctt">(.*?)</span>.*?>赞\[(\d+)]</a>&nbsp;<a href="(.*?)">转发\[(\d+)]</a>&nbsp;<a href="(.*?)" class="cc">评论\[(\d+)]</a>.*?<span class="ct">(.*?)&nbsp'
                            )

                            issuer_id_name_patternts = re.compile(
                                '<a class="nk" href="http://weibo.cn/(.*?)">(.*?)</a>')  # 匹配一段里面的名字和id
                            issuer_id_name = issuer_id_name_patternts.findall(item)
                            clean_issuer_id_patternts = re.compile('u/')
                            cleaned_issuer_id_name = re.sub(clean_issuer_id_patternts, '', issuer_id_name[0][0])
                            print "大v博文用户id和名字", cleaned_issuer_id_name, issuer_id_name[0][1]

                            issuer_blog_id_patternts = re.compile('id="(.*?)">')
                            issuer_blog_id = issuer_blog_id_patternts.findall(item)
                            print "博文id", issuer_blog_id[0]

                            issuer_blog_patternts = re.compile('<span class="ctt">:(.*?)>赞')
                            issuer_blog_unclean = issuer_blog_patternts.findall(item)
                            issuer_blog = self.cleaned_weibo(issuer_blog_unclean[0])
                            extra1 = re.compile('&nbsp;.*$')
                            cleaned_issuer_blog = re.sub(extra1, '', issuer_blog)
                            print "净化的博文", cleaned_issuer_blog

                            # 匹配点赞 转发 评论
                            like_forward_comment_patternts = re.compile(
                                '>赞\[(\d+)]</a>&nbsp;<a href="(.*?)">转发\[(\d+)]</a>&nbsp;<a href="(.*?)" class="cc">评论\[(\d+)]</a>')
                            like_forward_comment = like_forward_comment_patternts.findall(item)
                            print "点赞", like_forward_comment[0][0]
                            like_all_num += int(like_forward_comment[0][0])  # 计算总和，记录该话题的点赞规模
                            print "转发", like_forward_comment[0][2], like_forward_comment[0][1]
                            forward_all_num += int(like_forward_comment[0][2])  # 计算总和，记录该话题的转发规模
                            print "评论", like_forward_comment[0][4], like_forward_comment[0][3]
                            comment_all_num += int(like_forward_comment[0][4])  # 计算总和，记录该话题的评论规模
                            # 匹配时间
                            blog_time_paternts = re.compile('<!---->&nbsp;<span class="ct">(.*?)&nbsp;')
                            informality_blog_time = blog_time_paternts.findall(item)

                            if len(informality_blog_time) == 0:
                                blog_time_paternts1 = re.compile('<span class="ct">(.*?)</span>')
                                informality_blog_time = blog_time_paternts1.findall(item)

                            today_patternts = re.compile('今天')
                            minago_patternts = re.compile('\d+分钟前')
                            t = time.strftime('%m' + '月' + '%d' + '日', time.localtime())
                            t = t.decode('utf-8')
                            formality_blog_time = re.sub(today_patternts, t, informality_blog_time[0])
                            formality_blog_time = re.sub(minago_patternts, t, formality_blog_time)
                            if not formality_blog_time:
                                formality_blog_time = '0000-00-00'
                            try:
                                print "博文发表时间", formality_blog_time
                            except:
                                pass

                            # 爬取一条博文的转发路径，根据转发数
                            if int(like_forward_comment[0][2]) > 100:
                                forward_pages = 10  # ps

                            elif int(like_forward_comment[0][2]) <= 10:
                                forward_pages = 1

                            else:
                                if int(like_forward_comment[0][2]) % 10 > 0:
                                    forward_pages = int(like_forward_comment[0][2]) / 10 + 1
                                else:
                                    forward_pages = int(like_forward_comment[0][2]) / 10
                            reason_repeat_list = []
                            blog_origin = []
                            for forward_page in xrange(0, forward_pages):
                                f_page = forward_page + 1
                                forward_url = str(like_forward_comment[0][1]) + '&page=' + str(f_page)
                                print "转发链接", forward_url
                                reason_list = self.get_forward_common(forward_url)  # 爬取转发路径
                                reason_repeat_list += reason_list[0]
                                blog_origin.append(reason_list[1][0])
                            no_repeat_reason_list = list(set(reason_repeat_list))
                            no_repeat_reason_list.sort(key=reason_repeat_list.index)  # 去重后按时间顺序排序
                            print "新闻源：", blog_origin[0]

                            # 写入文本 txt_file
                            txt_file.write(
                                # self.weibo_topic
                                str(issuer_blog_id[0])  # '博文id：'
                                + '\n' + str(formality_blog_time)  # 博文时间
                                + '\n' + str(cleaned_issuer_blog)  # 博文
                                + '\n' + str(cleaned_issuer_id_name)  # 首发者的id
                                + '\n' + str(issuer_id_name[0][1])  # 首发者的名字
                                # + "\n点赞:" + like_forward_comment[0][0]  # 该博文的点赞量
                                # + "\n转发:" + like_forward_comment[0][2]  # 该博文的转发量
                                # + "\n评论:" + like_forward_comment[0][4]  # 该博文的评论量
                                + '\n' + str(blog_origin[0])
                                + '\n')
                            print 'hereaaaaa',issuer_blog_id[0],self.event_id
                            content_keywords = Keyword().combine_keywords(cleaned_issuer_blog)
                            print 'content_keywords',content_keywords
                            Database().save_content(str(issuer_blog_id[0]),str(formality_blog_time),self.event_id,str(cleaned_issuer_blog),str(content_keywords))
                            a=Content()
                            rows = a.get_content(self.event_id)
                            a.save_event_rest(rows,zhuti,topic,self.link,self.event_id)
                            Database().save_network_scale(self.event_id,corpus_dir,label_dir)
                            for reason in no_repeat_reason_list:  # 爬取转发路径，存储转发路径
                                print "转发理由：", reason
                                txt_file.write(str(reason) + '\n')
                            txt_file.write('\n')

                        else:
                            issuer_id_name_patternts = re.compile(
                                '<a class="nk" href="http://weibo.cn/(.*?)">(.*?)</a>')  # 匹配一段里面的名字和id
                            issuer_id_name = issuer_id_name_patternts.findall(item)
                            print "非大v博文用户id和名字", issuer_id_name[0][0], issuer_id_name[0][1]

                print "该话题的点赞规模", like_all_num
                print "该话题的转发规模", forward_all_num
                print "该话题的评论规模", comment_all_num
                Database().save_increment(self.event_id, comment_all_num, forward_all_num, like_all_num)
                txt_file.write("\n-----------------"
                               + "\n该话题的点赞规模:" + str(like_all_num)
                               + "\n该话题的转发规模:" + str(forward_all_num)
                               + "\n该话题的评论规模:" + str(comment_all_num))

                txt_file.close()

                print "文本写入完毕"
                print "转发该话题的转发者是大的v个数：", big_v_num

                return True
            else:
                print "搜索结果少于10个，直接忽略", hot_url
                return False

    def get_comment(self, key, value):
        """
        爬取每条微博的评论
        :return:comment
        """
        comment_file = open(self.comment_dir + 'uid=' + str(key[0]) + '.txt', 'w+')
        id_list = []
        user_name_list = []
        comment_list = []
        for i in value:
            for j in i:
                print "id,时间,博文id,博文,点赞,转发链接,转发量,评论链接,评论量", key[0], j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7]
                url = j[6]
                print "评论链接j[5]", url

                req = urllib2.Request(url=url, headers=self.header)
                comment_page = urllib2.urlopen(req).read()
                comment_patterns = re.compile(
                    '<div class="c" id="C.*?<a href="/u/(.*?)">(.*?)</a>.*?<span class="ctt">(.*?)</span>')

                comment = comment_patterns.findall(comment_page)

                print "博文为：", j[1] + ' ' + j[2]
                print "以下是该博文的评论"
                comment_file.write("博文id为： " + j[1] + ' ' + j[2] + '\n' + "以下是该博文的评论： " + '\n')
                for k in comment:
                    link_patterns = re.compile('<.*?>')
                    kk = re.sub(link_patterns, "", k[2])
                    print 'id:', k[0], '用户名:', k[1], '评论:', kk
                    # id_list.append(k[0])
                    # user_name_list.append(k[1])
                    # comment_list.append(kk)
            # id_name_comment = zip(id_list,user_name_list,comment_list)
                    comment_file.write(
                        "id: " + str(k[0]) + ', 用户名： ' + str(k[1]) + ', 评论： ' + str(kk) + '\n')

            comment_file.close()
        return True

    def get_forward_path(self, key, value):
        """
        爬取每条博文的转发路径
        :param key:
        :param value:
        :return:
        """
        for i in value:
            forward_path_file = open(self.forward_path_dir + 'uid=' + str(key[0]) + '.txt', 'w+')
            for j in i:
                print "id,时间,博文id,博文,点赞,转发链接,转发量,评论链接,评论量", key[0], j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7]
                url = j[4]
                print "博文为：", j[1] + ' ' + j[2]
                print "该转发链接： ", url
                req = urllib2.Request(url=url, headers=self.header)
                forward_page = urllib2.urlopen(req).read()

                # 通过原文评论链接找到原文转发链接，从而找到转发路径
                if "转发了" in forward_page:
                    original_comment_url_patterns = re.compile(
                        '<span class="cmt">原文转发.*?<a href="(.*?)" class="cc">原文评论\[(.*?)]')
                    original_comment_url = original_comment_url_patterns.findall(forward_page)
                    comment_url = "http://weibo.cn" + original_comment_url[0][0]
                    # print "该博文原文评论链接： ", comment_url

                    # 进入原文评论页面，找到转发的链接
                    req = urllib2.Request(url=comment_url, headers=self.header)
                    original_comment_page = urllib2.urlopen(req).read()
                    original_forward_url_patterns = re.compile(
                        '<a href="/repost(.*?);#rt">转发\[(.*?)]</a>')  # 匹配转发链接和转发数量
                    original_forward_url = original_forward_url_patterns.findall(original_comment_page)

                    # 匹配第一个转发博文的用户
                    first_forwarder_patterns = re.compile(
                        '<div class="c" id="M_"><div>    <a href=".*?">(.*?)</a>.*?<a href="/repost/.*?uid=(.*?)&amp;.*?转发')
                    first_forwarder = first_forwarder_patterns.findall(original_comment_page)
                    print first_forwarder
                    print "首发者的用户名,id： ", first_forwarder[0][0], first_forwarder[0][1]
                    forward_path_file.write(
                        "博文为： " + j[1] + ' ' + j[2] + '\n' + "首发者的用户名,id： " + first_forwarder[0][0] + "," +
                        first_forwarder[0][1] + '\n')
                    print "该博文原文转发链接： ", "http://weibo.cn/repost" + original_forward_url[0][0]
                    print "以下是该博文的转发人及转发理由："
                    if int(original_forward_url[0][1]) > 50:
                        repeat_list = []
                        blog_origin = []
                        print "转发量：", original_forward_url[0][1]
                        for page in xrange(1, int(original_forward_url[0][1]) / 10):  # 翻页
                            forward_url = "http://weibo.cn/repost" + original_forward_url[0][0] + "&page=" + str(page)
                            print forward_url
                            forward_string = self.get_forward_common(forward_url)
                            # print "调用时", len(forward_string)
                            repeat_list += forward_string[0]
                            # print "我就看看",len(repeat_list)
                            blog_origin.append(forward_string[1][0])

                        # print "大去重前", len(repeat_list)
                        no_repeat = list(set(repeat_list))
                        no_repeat.sort(key=repeat_list.index)
                        print "大去重后", len(no_repeat)
                        print "新闻源：", blog_origin[0]
                        forward_path_file.write(str(blog_origin[0]) + '\n')
                        for item in no_repeat:
                            print item
                            forward_path_file.write(item + '\n')

                else:
                    print "此条链接是首发链接"
                    first_forwarder_patterns = re.compile(
                        '<div class="c" id="M_"><div>    <a href=".*?">(.*?)</a>.*?<a href="/comment.*?&amp;uid=(.*?)&amp;#cmtfrm')
                    first_forwarder = first_forwarder_patterns.findall(forward_page)
                    print first_forwarder
                    print "首发者的用户名,id： ", first_forwarder[0][0] + " " + first_forwarder[0][1]
                    forward_path_file.write(
                        "博文为： " + j[1] + ' ' + j[2] + '\n' + "首发者的用户名,id： " + first_forwarder[0][0] + "," +
                        first_forwarder[0][1] + '\n')
                    print "转发量：", j[5]
                    if int(j[5]) > 50:
                        repeat_list = []
                        blog_origin = []
                        for page in xrange(1, int(j[5]) / 10):
                            forward_url = j[4] + "&page=" + str(page)
                            print forward_url
                            forward_string = self.get_forward_common(forward_url)
                            repeat_list += forward_string[0]
                            print "我就看看", len(repeat_list)

                            blog_origin.append(forward_string[1][0])

                        # print "大去重前", len(repeat_list)
                        no_repeat = list(set(repeat_list))
                        no_repeat.sort(key=repeat_list.index)
                        print "大去重后", len(no_repeat)
                        print "新闻源：", blog_origin[0]
                        forward_path_file.write(str(blog_origin[0]) + '\n')

                        for item in no_repeat:
                            print item
                            forward_path_file.write(item + '\n')
            forward_path_file.close()
        return True

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
        time.sleep(int(random.uniform(0,5)))

        forward_path = forward_patterns.findall(forward_page)

        blog_origin_patternts = re.compile('>(http://t.cn/.*?)</a></span>')
        blog_origin = blog_origin_patternts.findall(forward_page)

        if len(blog_origin) > 0:
            blog_origin = [re.sub(useless,'',blog_origin[0])]
            self.link = blog_origin[0]

        if len(blog_origin) == 0:
            blog_origin.append(str(None))

        forward_string_list = []
        for k in forward_path:

            k0 = re.sub(label_pattern,'',k[0])
            kk = re.sub(other_patterns, "", k[1])
            forward_reason1 = re.sub(label_pattern, "", kk)
            forward_reason2 = re.sub(link_pattern,'',forward_reason1)
            forward_reason = re.sub(space_pattern,'',forward_reason2)

            forward_string = str(k0) + ": " + str(forward_reason)
            forward_string_list.append(forward_string)
        # print "小去重前", len(forward_string_list)
        no_repeat_list = list(set(forward_string_list))
        no_repeat_list.sort(key=forward_string_list.index)
        # print "小去重后", len(no_repeat_list)
        return no_repeat_list, blog_origin  # 返回转发路径和博文源

def main_weibo():
    MoblieWeibo().login('', '')

    account = {
        "人民日报": 2803301701, "新浪新闻": 2028810631, "凤凰周刊": 1267454277,
        "网易新闻客户端": 1974808274, "北京晨报": 1646051850,
        "头条新闻": 1618051664, "人民网": 2286908003,
        "财经网": 1642088277, "新京报": 1644114654, "环球时报": 1974576991,
        "中国新闻网": 1784473157, "三联生活周刊": 1191965271, "法制晚报": 1644948230,
        "新闻晨报": 1314608344, "中国之声": 1699540307, "中国新闻周刊": 1642512402,
        "澎湃新闻": 5044281310, "中国日报": 1663072851, "北京青年报": 1749990115,
        "新快报": 1652484947, "华西都市报": 1496814565, "凤凰网": 2615417307,
        "FT中文网": 1698233740,
    }

    rand_account = random.sample(account, 5)  # 从 account 中随机获取5个元素，作为一个片断返回

    for acc in rand_account:
        print "当前猎头：", acc, account[acc]
        weibo_page = WeiboPage(account[acc])

        a = multiprocessing.Process(target=weibo_page.get_page, args=(1, 2))
        a.start()

    a.join()
    print '完成多进程'

