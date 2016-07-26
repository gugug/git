# coding=utf-8
from crawl_weibo import *

__author__ = 'gu'

class GetHunterForwardPath(WeiboPage):
    """
    这个是用来只分析猎头的博文的转发路径，即是没有进行进一步的搜索再爬取路径
    """
    def get_hunter_forward_path(self, key, value):
        """
        爬取每条博文的转发路径
        :param key: 猎头的id
        :param value: 猎头的每一条博文信息 （id,时间,博文id,博文,点赞,转发链接,转发量,评论链接,评论量）
        :return:
        """
        for i in value:
            forward_path_file = open(self.forward_path_dir + 'uid=' + str(key[0]) + '.txt', 'w+')
            for j in i:
                # print "id,时间,博文id,博文,点赞,转发链接,转发量,评论链接,评论量", key[0], j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7]
                url = j[4]
                # print "博文为：", j[1] + ' ' + j[2]
                # print "该转发链接： ", url
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

