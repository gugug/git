# coding=utf-8
import re
import urllib2
from class_weibo import WeiboPage
__author__ = 'gu'

class GetComment(WeiboPage):
    """
    这个是用来爬取猎头博文的评论的
    """
    def get_comment(self, key, value):
        """
        爬取每条微博的评论
        :return:comment
        """
        comment_file = open(self.comment_dir + 'uid=' + str(key[0]) + '.txt', 'w+')
        # id_list = []
        # user_name_list = []
        # comment_list = []
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

