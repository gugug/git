# coding=utf-8
from class_weibo import *
from get_forward_path import *
from get_hunter_weibo import *

__author__ = 'gu'


class SearchTopic(WeiboPage):
    """
    通过猎头发现的话题事件，进行话题提取和关键词提取，进行搜索并爬取路径
    """

    def get_search_topic(self, uid, tuple):
        """
        此方法用来判断话题是否为热点，是热点则进行下一步的路径分析爬取
        :param uid: 猎头的id
        :param tuple: (话题 微博关键字 话题id) 组成的元组，进行绑定
        :return: 布尔值，是热点就返回true,不是热点就返回false
        """

        zhuti = tuple[0]  # 话题
        topic = tuple[1]  # 微博关键字
        blog_id = tuple[2]  # 话题id

        print "正在搜索话题关键词: ", topic
        hot_url = 'http://weibo.cn/search/mblog/?keyword=' + str(
            urllib2.quote(topic)) + '&sort=hot'
        print 'hot', hot_url
        req = urllib2.Request(url=hot_url, headers=self.header)
        result_page = urllib2.urlopen(req).read()

        if "抱歉，未找到" in result_page:
            req = urllib2.Request(url=hot_url, headers=self.header)
            result_page = urllib2.urlopen(req).read()
            if "抱歉，未找到" in result_page:
                print "看来真的没有结果了~~~"
                return False

        if "抱歉，未找到" not in result_page:
            result_num_pattern = re.compile('<span class="cmt">共(.*?)条</span>')
            result_num = result_num_pattern.findall(result_page)
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
                print 'checking topic', check
                if check:
                    self.event_id = 'topic' + blog_id
                else:
                    self.event_id = check
                print "self.event_id+blog_id", self.event_id
                self.topic = zhuti
                Event().save_event_id(self.event_id)
                Database().save_participate(self.one_user, self.event_id)

                self.short_dir = create_time_file(zhuti)  # 动态生成话题文件夹，全局变量
                label_dir = self.short_dir + 'new_label_link.xls'

                corpus_dir = DOC_DIR + '/' + self.short_dir + 'uid=' + str(uid) + '.txt'
                print "生成的动态目录：", corpus_dir
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
                    print "搜索结果的链接", pageurl

                    req = urllib2.Request(url=pageurl, headers=self.header)
                    result_turn_page = urllib2.urlopen(req).read()
                    issuer_pattern = re.compile('<div class="c" (id.*?)<div class="s"></div>')  # 把每个人的一个整个匹配下来
                    issuer = issuer_pattern.findall(result_turn_page)
                    for item in issuer:
                        if 'alt="V"/>' in item:
                            big_v_num += 1  # 记录大v的个数

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

                            # result_list = [str(issuer_blog_id[0]), str(formality_blog_time), str(cleaned_issuer_blog),
                            #               str(cleaned_issuer_id_name), str(issuer_id_name[0][1]), str(blog_origin[0])]
                            # write_search_result(corpus_dir,result_list)

                            # 写入文本 txt_file
                            txt_file.write(
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

                            print 'hereaaaaa', issuer_blog_id[0], self.event_id

                            content_keywords = Keyword().combine_keywords(cleaned_issuer_blog)  # 把博文进行关键词提取
                            print 'content_keywords', content_keywords

                            Database().save_content(str(issuer_blog_id[0]), str(formality_blog_time), self.event_id,
                                                    str(cleaned_issuer_blog), str(content_keywords))
                            a = Content()
                            rows = a.get_content(self.event_id)
                            a.save_event_rest(rows, zhuti, topic, self.link, self.event_id)
                            Database().save_network_scale(self.event_id, corpus_dir, label_dir)

                            # write_search_result(corpus_dir, no_repeat_reason_list)

                            for reason in no_repeat_reason_list:  # 爬取转发路径，存储转发路径
                                print "转发理由：", reason
                                txt_file.write(str(reason) + '\n')
                            txt_file.write('\n')

                        else:
                            issuer_id_name_pattern = re.compile(
                                '<a class="nk" href="http://weibo.cn/(.*?)">(.*?)</a>')  # 匹配一段里面的名字和id
                            issuer_id_name = issuer_id_name_pattern.findall(item)
                            print "非大v博文用户id和名字", issuer_id_name[0][0], issuer_id_name[0][1]

                print "该话题的点赞规模", like_all_num
                print "该话题的转发规模", forward_all_num
                print "该话题的评论规模", comment_all_num

                Database().save_increment(self.event_id, comment_all_num, forward_all_num, like_all_num)

                # all_num = [str(like_all_num), str(forward_all_num), str(comment_all_num)]
                # write_search_result(corpus_dir, all_num)

                txt_file.write("\n-----------------"
                               + "\n该话题的点赞规模:" + str(like_all_num)
                               + "\n该话题的转发规模:" + str(forward_all_num)
                               + "\n该话题的评论规模:" + str(comment_all_num))

                txt_file.close()

                print "文本写入完毕"
                print "转发该话题的转发者是大的v个数：", big_v_num
            else:
                print "搜索结果少于10个，直接忽略", hot_url

# def write_search_result(dir_file, list_result):
#     """
#     把列表的内容写进文档, 不过这样方法会打开文件几次，速度上满了3倍左右
#     """
#     txt_file = open(dir_file, 'a+')
#     for i in list_result:
#         txt_file.write(str(i) + '\n')
#     txt_file.write('\n')
#     txt_file.close()
