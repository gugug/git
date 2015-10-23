#coding=utf-8
__author__ = 'gu'
import urllib2
import re
from class_login import Login
header_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0'
headers = {
    'User-Agent': header_agent
}

def im_login():
    Login().slogin()

def getHostUrl():
        b = 600000
        HostUrl="http://weibo.cn/u/2995631244"
        UrlRequest=urllib2.Request(HostUrl,headers=headers)
        response=urllib2.urlopen(UrlRequest)
        text=response.read()
        page = re.compile('跳页" />.*?/(.*?)页')
        num = page.findall(text)
        pm = int(num[0])

        if b>pm:
            b = pm
        else:
            pass
        print b




im_login()
getHostUrl()


