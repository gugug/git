# coding=utf-8


from crawl_weibo import *
from get_forward_path import *
from get_hunter_weibo import *


class SearchTopic(WeiboPage):
    """
    通过猎头发现的话题事件，进行话题提取和关键词提取，进行搜索并爬取路径
    """

    def is_heated_topic(self, tpw):
        """
        此方法用来判断话题是否为热点，是热点则进行下一步的路径分析爬取
        :param uid:
        :param tuple:
        :return:
        """
        topic_words = tpw

        print "正在搜索话题关键词: ", topic_words
        hot_url = 'http://weibo.cn/search/mblog/?keyword=' + str(
            urllib2.quote(topic_words)) + '&sort=hot'
        req = urllib2.Request(url=hot_url, headers=self.header)
        result_page = urllib2.urlopen(req).read()

        if "抱歉，未找到" not in result_page:
            result_num_pattern = re.compile('<span class="cmt">共(.*?)条</span>')
            result_num = result_num_pattern.findall(result_page)
            if not result_num:
                result_num.append(1)
            # print "result_num", result_num[0]

            if int(result_num[0]) > 1000:
                page_num = 60  # ps
                # print "有", result_num[0], "条结果,判断为热点新闻"
            elif int(result_num[0]) <= 10:
                page_num = 0
            else:
                if int(result_num[0]) % 10 > 0:
                    page_num = int(result_num[0]) / 10 + 1
                else:
                    page_num = int(result_num[0]) / 10
                # print "有", result_num[0], "条结果,判断为热点新闻"
            return page_num

        else:
            req = urllib2.Request(url=hot_url, headers=self.header)
            result_page = urllib2.urlopen(req).read()
            if "抱歉，未找到" in result_page:
                # print "看来真的没有结果了~~~"
                return False

    def get_id_name(self, item):
        """
        大v博文用户id和名字
        :param item:一个人的全部待匹配源代码
        :return:大v的id,大v的名字
        """
        issuer_id_name_patterns = re.compile('<a class="nk" href="http://weibo.cn/(.*?)">(.*?)</a>')  # 匹配一段里面的名字和id
        issuer_id_name = issuer_id_name_patterns.findall(item)
        clean_issuer_id_patterns = re.compile('u/')
        cleaned_issuer_id_name = re.sub(clean_issuer_id_patterns, '', issuer_id_name[0][0])
        return cleaned_issuer_id_name, issuer_id_name[0][1]

    def get_blog_id(self, item):
        """
        博文id
        :param item:一个人的全部待匹配源代码
        :return:博文id
        """
        issuer_blog_id_patternts = re.compile('id="(.*?)">')
        issuer_blog_id = issuer_blog_id_patternts.findall(item)
        return issuer_blog_id[0]

    def get_content(self, item):
        """
        博文内容
        :param item:一个人的全部待匹配源代码
        :return:博文内容
        """

        issuer_blog_patternts = re.compile('<span class="ctt">:(.*?)>赞')
        issuer_blog_unclean = issuer_blog_patternts.findall(item)
        issuer_blog = self.cleaned_weibo(issuer_blog_unclean[0])
        extra1 = re.compile('&nbsp;.*$')
        cleaned_issuer_blog = re.sub(extra1, '', issuer_blog)
        return cleaned_issuer_blog

    def get_nums(self, item):
        """
        :param item:一个人的全部待匹配源代码
        :return:点赞 转发 评论 转发路径
        """
        like_forward_comment_patternts = re.compile(
            '>赞\[(\d+)]</a>&nbsp;<a href="(.*?)">转发\[(\d+)]</a>&nbsp;<a href="(.*?)" class="cc">评论\[(\d+)]</a>')
        like_forward_comment = like_forward_comment_patternts.findall(item)
        # print "点赞", like_forward_comment[0][0]
        self.like_all_num += int(like_forward_comment[0][0])  # 计算总和，记录该话题的点赞规模
        # print "转发", like_forward_comment[0][2], like_forward_comment[0][1]
        self.forward_all_num += int(like_forward_comment[0][2])  # 计算总和，记录该话题的转发规模
        # print "评论", like_forward_comment[0][4], like_forward_comment[0][3]
        self.comment_all_num += int(like_forward_comment[0][4])  # 计算总和，记录该话题的评论规模
        return like_forward_comment[0][0], like_forward_comment[0][2], like_forward_comment[0][4], \
               like_forward_comment[0][1]

    def get_time(self, item):
        """
        :param item:一个人的全部待匹配源代码
        :return:发表时间
        """
        try:
            blog_time_pattern = re.compile('<!---->&nbsp;<span class="ct">(.*?)&nbsp;')
            informality_blog_time = blog_time_pattern.findall(item)
            if len(informality_blog_time) == 0:
                blog_time_pattern1 = re.compile('<span class="ct">(.*?)</span>')
                informality_blog_time = blog_time_pattern1.findall(item)
            today_pattern = re.compile('今天')
            minago_pattern = re.compile('\d+分钟前')
            t = time.strftime('%m' + '月' + '%d' + '日', time.localtime())
            t = t.decode('utf-8')
            formality_blog_time = re.sub(today_pattern, t, informality_blog_time[0])
            formality_blog_time = re.sub(minago_pattern, t, formality_blog_time)
            if not formality_blog_time:
                formality_blog_time = '0000-00-00'
            return formality_blog_time
        except:
            pass

    def get_origin(self, fwd_num, fwd_link):
        """
        :param fwd_num:转发数
        :param fwd_link:转发链接
        :return:传播源 转发原因
        """
        reason_repeat_list = []
        blog_origin = []
        if int(fwd_num) > 100:
            forward_pages = 60  # ps
        elif int(fwd_num) <= 10:
            forward_pages = 1
        else:
            if int(fwd_num) % 10 > 0:
                forward_pages = int(fwd_num) / 10 + 1
            else:
                forward_pages = int(fwd_num) / 10

        for forward_page in xrange(0, forward_pages):
            f_page = forward_page + 1
            forward_url = str(fwd_link) + '&page=' + str(f_page)

            reason_list = self.get_forward_common(forward_url)  # 爬取转发路径

            reason_repeat_list += reason_list[0]
            blog_origin.append(reason_list[1][0])

            no_repeat_reason_list = list(set(reason_repeat_list))
            no_repeat_reason_list.sort(key=reason_repeat_list.index)  # 去重后按时间顺序排序
            return blog_origin[0], no_repeat_reason_list

    def get_topic(self, content):
        """
        :param content:博文内容
        :return:博文主题
        """
        topic_patternts = re.compile('【(.*?)】')
        topic = topic_patternts.findall(content)
        if len(topic) > 0:
            topic_clean_pattern = re.compile('(\[.*?])')
            topic = re.sub(topic_clean_pattern, '', topic[0])
            topic_clean3_pattern = re.compile('#')
            topic = re.sub(topic_clean3_pattern, '', topic)
            topic_clean2_pattern = re.compile('\\s')
            topic_result = re.sub(topic_clean2_pattern, '', topic)

        else:
            # print "这篇博文没有话题，检测不到事件"
            topic_result = '未知'
        return topic_result

    def search_topic(self, blogid, tbwtuple):
        """
        对
        :param blogid: 一个事件类的id
        :param tbwtuple: 元组（类的博文标题, 博文, 关键词）
        :return:3个列表, s相同索引下的内容是对应的
            # total_result_list = [[博文id,博文时间,标题,博文,关键词,首发者的id,首发者的名字,点赞,转发,评论,origin], ]
            # total_reason_list = [[asd@fadsf@人民日报, safagr@人民日报, yutsfa@人民日报], ]
            # lfc_all_num = [该话题的点赞规模,该话题的转发规模,该话题的评论规模]
        """

        topic_words = tbwtuple[2]  # 微博关键字
        bid = blogid  # 原id

        total_result_list = []  # [(title1,blog1,word1),(title2,blog2,word2)] 一个元组中word搜索出来的全部和
        total_reason_list = []
        lfc_all_num = []

        big_v_num = 0
        self.like_all_num = 0
        self.forward_all_num = 0
        self.comment_all_num = 0
        page_num = self.is_heated_topic(topic_words)

        if page_num > 0:
            for page in xrange(0, page_num):
                page = int(page) + 1
                pageurl = 'http://weibo.cn/search/mblog?keyword=' + str(
                    urllib2.quote(topic_words)) + '&sort=hot&page=' + str(page)

                req = urllib2.Request(url=pageurl, headers=self.header)
                result_turn_page = urllib2.urlopen(req).read()
                issuer_pattern = re.compile('<div class="c" (id.*?)<div class="s"></div>')  # 把每个人的一个整个匹配下来
                issuer = issuer_pattern.findall(result_turn_page)

                for item in issuer:
                    rpt_reason_list = []

                    if 'alt="V"/>' in item:
                        big_v_num += 1  # 记录大v的个数
                        user_id, user_name = self.get_id_name(item)
                        blog_id = self.get_blog_id(item)
                        content = self.get_content(item)
                        topic = self.get_topic(content)
                        like_num, rpt_num, cmt_num, path = self.get_nums(item)
                        ptime = self.get_time(item)
                        origin, no_repeat_reason_list = self.get_origin(rpt_num, path)
                        kw = Keyword()
                        keywords = kw.combine_keywords(content)
                        topic_words = kw.combine_keywords(topic)

                        result_list = [blog_id, ptime, topic, content, keywords, user_id, user_name,
                                       like_num, rpt_num, cmt_num, origin]

                        total_result_list.append(result_list)

                        for reason in no_repeat_reason_list:  # 爬取转发路径，存储转发路径
                            rpt_reason_list.append(str(reason) + '@' + user_name+":")

                        total_reason_list.append(rpt_reason_list)

                    else:
                        issuer_id_name_pattern = re.compile(
                            '<a class="nk" href="http://weibo.cn/(.*?)">(.*?)</a>')  # 匹配一段里面的名字和id
                        issuer_id_name = issuer_id_name_pattern.findall(item)
                        # print "非大v博文用户id和名字", issuer_id_name[0][0], issuer_id_name[0][1]

            lfc_all_num.append(self.like_all_num)
            lfc_all_num.append(self.forward_all_num)
            lfc_all_num.append(self.comment_all_num)

            # print "转发该话题的转发者是大的v个数：", big_v_num
        else:
            # print "搜索结果少于10个，直接忽略"
            lfc_all_num = [0, 0, 0]  # 不是热点，规模初始值为0
        return total_result_list, total_reason_list, lfc_all_num

    # def event_clustering(self, bid, eid):  # 等嘉琳来更新真正的聚类
    #     eid = 'tp' + str(eid)
    #     db_cnt = Content()
    #     db_cnt.update_eid(bid, eid)
