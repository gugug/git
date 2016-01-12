#!/usr/bin/env python
# coding:utf-8
__author__ = 'shoufu'

'''
@version: 2.7.6
@date: 2015-10-12
@function: 
'''

import os
import re
import urllib


class MoblieWeiboLogin:
    def __init__(self):
        # self.downloader = Downloader()

        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/35.0'}
        self.url = 'http://weibo.cn/'
        self.count = 0

    def getHostUrl(self):
        HostUrl = "http://weibo.cn/reg/index"
        pageCode = self.downloader.getPageCode(HostUrl)

        pattern = re.compile('<a href="(.*?)">登录</a>')
        self.HostUrl = re.search(pattern, pageCode).group(1)

    def getArgs(self):
        self.getHostUrl()
        pageCode = self.downloader.getPageCode(self.HostUrl)

        UrlPattern = re.compile("<form action=\"(.*?)\" method=\"post\">", re.S)
        self.Url = 'http://login.weibo.cn/login/' + re.search(UrlPattern, pageCode).group(1)

        vkPattern = re.compile('<input type="hidden" name="vk" value="(.*?)" />')
        self.vk = re.search(vkPattern, pageCode).group(1)

        self.BackUrlPattern = re.compile("<input type=\"hidden\" name=\"backURL\" value=\"(.*?)\" />")
        self.BackUrl = re.search(self.BackUrlPattern, pageCode).group(1)

        randPattern = re.compile('<form action="\?rand=(.*?)&')
        self.rand = re.search(randPattern, pageCode).group(1)

        pwdPattern = re.compile('<input type="password" name="(.*?)" size="30" />')
        self.passwd = re.search(pwdPattern, pageCode).group(1)

    def login(self, username, password):
        self.getArgs()
        PostData = {
            "mobile": username,
            str(self.passwd): password,
            'submit': "登录",
            'remember': "on",
            'backURL': self.BackUrl,
            'vk': self.vk,
            'tryCount': '',
            'rand': self.rand
        }
        PostData = urllib.urlencode(PostData)
        pageCode = self.downloader.getPageCode(self.Url, PostData)
        login_error = re.findall('登录名或密码错误', pageCode)
        login_failed = re.findall('加入新浪微博,分享新鲜的事',pageCode)
        if login_error:
            print '登录名或密码错误'
            os._exit(0)
        elif login_failed:
            print 'Login Failed!!'
            os._exit(0)
        else:
            print 'login success!!'
            print pageCode
            return True

    def isBanned(self, pageCode):
        hot_weibo = re.findall('微博广场', pageCode)
        is_banned = re.findall('@手机微博 为您解答使用问题', pageCode)
        if hot_weibo and is_banned:
            return True
        return False


if __name__ == '__main__':
    login = MoblieWeiboLogin()
    login.login('13620859694', 'tttt5555')
#     import init.utils as utils
#     list = utils.read_file('account/weibo.txt')
#     for num, item in enumerate(list):
#         print num, item