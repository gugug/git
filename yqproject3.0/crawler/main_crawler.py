# coding=utf-8
__author__ = 'gu'
from class_weibo import *
from updater import *
from detection import *
from search_topic import *


class Run(WeiboPage):
    """
    程序的启动器，先调用更新器进行之前话题的更新，然后更新完毕后进行新的检测新的话题事件
    """
    def run(self):
        """
            调用更新方法，更新完毕后进行新话题检测
            :return:
        """
        print "再次更新长度为x的话题", len(WeiboPage.afore_all_uid)
        if WeiboPage.afore_all_uid:
            print "开始更新"
            Update(self.one_user).update()
        else:
            print "无内容，不更新，开始检测"
        detection()


def main_weibo():
    MoblieWeibo().login('', '')
    while True:
        Run(2803301701).run()
        print "即将休息一下"
        sleep(2)
        print "睡醒"

main_weibo()
