#coding:utf-8
__author__ = 'chenge'
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","dbtest2.settings")
django.setup()


import re,random
import urllib2,urllib,cookielib

class MoblieWeibo:  #模拟登陆
    def __init__(self):
        self.cj = cookielib.LWPCookieJar()
        # if cookie_filename is not None:
        #     self.cj.load(cookie_filename)
		#将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
        self.cookie_processor = urllib2.HTTPCookieProcessor(self.cj)
        #创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
        self.opener = urllib2.build_opener(self.cookie_processor, urllib2.HTTPHandler)
        #将包含了cookie、http处理器、http的handler的资源和urllib2对象绑定在一起
        urllib2.install_opener(self.opener)
        self.headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/35.0'}

    def getHostUrl(self):
        HostUrl="http://weibo.cn/pub/"
        UrlLoginRequest=urllib2.Request(HostUrl,headers=self.headers)
        response=urllib2.urlopen(UrlLoginRequest)
        text=response.read()

        pattern=re.compile('<a href=\'(http://login.weibo.cn/login/?.*?)\'>登录</a>')
        self.HostUrl=re.search(pattern,text).group(1)
        # print "登录入口Url:"
        # print self.HostUrl

    def getArgs(self):

        self.getHostUrl()
        ArgsRequest=urllib2.Request(self.HostUrl,headers=self.headers)
        response=urllib2.urlopen(ArgsRequest)
        text=response.read()

        # print "在登录入口获取需要post数据的页面"
        UrlPattern=re.compile("<form action=\"(.*?)\" method=\"post\">",re.S)
        self.Url='http://login.weibo.cn/login/?backURL=&backTitle=&vt=4&revalid='+'&ns=1'
        # print self.Url

        # print "获取post数据中的vk的值:"
        vkPattern=re.compile('<input type="hidden" name="vk" value="(.*?)" />')
        self.vk=re.search(vkPattern,text).group(1)
        # print self.vk

        # print "获取post数据中的backURL的值:"
        self.BackUrlPattern=re.compile("<input type=\"hidden\" name=\"backURL\" value=\"(.*?)\" />")
        self.BackUrl=re.search(self.BackUrlPattern,text).group(1)
        # print self.BackUrl

        # print "获取post数据中的rand的值:"
        randPattern=re.compile('<form action="\?rand=(.*?)&')
        self.rand=re.search(randPattern,text).group(1)
        # print self.rand

        # print "获取post数据中的passwd变量的值:"
        pwdPattern=re.compile('<input type="password" name="(.*?)" size="30" />')
        self.passwd=re.search(pwdPattern,text).group(1)
        # print self.passwd
    def login(self,username,password):
        self.getArgs()
        # print "生成post数据,向网址Url提交post:"
        PostData={
            "mobile":username,
            str(self.passwd):password,
            'submit':"登录",
            'remember':"on",
            'backURL':self.BackUrl,
            'vk':self.vk,
            'tryCount':'',
            'rand':self.rand
        }
        # print PostData
        PostData=urllib.urlencode(PostData)
        # print "输出调交post返回的主页:"
        request=urllib2.Request(self.Url,PostData,self.headers)
        response=urllib2.urlopen(request)
        text=response.read()
        # print text
