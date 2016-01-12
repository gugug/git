# -*- coding: utf-8 -*-
__author__ = 'K'

import urllib2
import random
import time
import re


def getIpFromYDL():
    setIpProxy(getIpInFile())  # 设置代理
    headers = {
        'Accept': "text/css,*/*;q=0.1",
        'Connection': "keep-alive",
        'Host': "www.youdaili.net",
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'
    }

    req1 = urllib2.Request(
        url='http://www.youdaili.net/Daili/',
        headers=headers
    )

    proxyTypeDict = {'chinaProxy': "【国内代理】"}
    # 'foreignProxy': "【国外代理】"}  # 可添加  'socksProxy' : "【Socks代理】" ,'httpProxy' : "【HTTP代理】"
    proxyTypeUrlDict = {}
    try:
        req = urllib2.urlopen(req1, timeout=20)
        respon = req.read()
        # print "respon",respon

        for key in proxyTypeDict.keys():
            pattern = '<li><a href="(.*?)" target="_blank"><font color=#FF7300>' + proxyTypeDict[key] + '</font>'
            url = re.search(pattern, respon).group(1)  # search()从字符串开始寻找，直到匹配到正则，返回第一个括号匹配的的
            print "url",url
            proxyTypeUrlDict.setdefault(key, url)  # 和get()方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值。
    except:  # 有些代理不能用导致异常，返回0表示失败
        return 0
    for proxyType in proxyTypeUrlDict.keys():
        YDL(proxyType, proxyTypeUrlDict[proxyType])
        time.sleep(20)
    return 1


def YDL(proxyType, url):
    proxyList = []
    stateList = []
    headers = {
        'Accept': "text/css,*/*;q=0.1",
        'Connection': "keep-alive",
        'Host': "www.youdaili.net",
        'Referer': "http://www.youdaili.net/Daili/",
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'
    }
    pattern = '<div class="cont_font">[\w\W]+?<p>([\w\W]+?)</p>'
    tempUrl = url.replace('.html', '')
    number = 1
    pageLen = 1
    while True:
        if number > pageLen:
            break
        if number == 1:
            url = tempUrl + '.html'
        else:
            url = tempUrl + "_" + str(number) + ".html"
        print url

        try:
            req1 = urllib2.Request(
                url=url,
                headers=headers
            )
            req = urllib2.urlopen(req1, timeout=20)
            respon = req.read()
            # print "第二个url",respon
            list = re.search(pattern, respon).group(1).split("<br />")
            print list
        except Exception, e:  # 有些代理异常，会出错
            print "e", e
            print proxyType, "Error! "
            setIpProxy(getIpInFile())
            time.sleep(20)
            continue
        '''
        if number == 1: #此代码可不要，要了之后，将爬取第二页以后的代理，第二页后的代理不知道是否有效。
            try:
                pageLen = int(re.search('共([\d]+)页: ',respon).group(1))
            except:
                pass
        time.sleep(20)
        '''
        number += 1
        for temp in list:
            print temp
            try:
                ip = temp.split("#")
                stateList.append(ip[1])
                ip = ip[0].split('@')
                if ip[1] == 'HTTP':
                    proxyList.append({'http': 'http://' + ip[0].replace("\r\n", '')})
                elif ip[1] == "HTTPS":
                    proxyList.append({'https': 'https://' + ip[0]})
                else:
                    pass
            except:
                pass
    fileProxyIp = open('./proxyIp/' + proxyType + 'Ip.txt', 'w')
    for i in range(len(proxyList)):
        fileProxyIp.write(stateList[i] + '#')
        temp = proxyList[i]
        fileProxyIp.write(str(temp))
        fileProxyIp.write('\r\n')
    fileProxyIp.flush()

    # 一般的文件流操作都包含缓冲机制，write方法并不直接将数据写入文件，而是先写入内存中特定的缓冲区。
    # flush方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区。
    # 正常情况下缓冲区满时，操作系统会自动将缓冲数据写入到文件中。
    # 至于close方法，原理是内部先调用flush方法来刷新缓冲区，再执行关闭操作，这样即使缓冲区数据未满也能保证数据的完整性。

    fileProxyIp.close()
    print proxyType, len(proxyList), "finish!"


def setIpProxy(ipProxyList):  # 设置代理
    ipProxy = ipProxyList[random.randint(0, len(ipProxyList) - 1)]
    print "任意取一条设置ip"
    # handlers = [urllib2.ProxyHandler({'http': 'http://%s/' % proxy})]
    proxy_support = urllib2.ProxyHandler(ipProxy)
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    # andlers = [urllib2.ProxyHandler({'http': 'http://%s/' % proxy})]
    # opener = urllib2.build_opener(*handlers)
    # response = opener.open(urllib2.quote(url, safe=":/"), timeout=30)


def clearIpProxy():  # 清除代理
    urllib2.install_opener(None)
    print "清除代理成功"


def getIpInFile():  # 从ip.txt文件中读取代理
    file = open("ip.txt", 'r')
    ipProxyList = []
    while True:
        temp = file.readline()
        if temp:
            ipProxyList.append(eval(temp))  # 将字符串str当成有效的表达式来求值并返回计算结果
            print "从ip.txt读取一行成功"
        else:
            print "ip.txt读取完毕"
            break
    return ipProxyList


def getProxyIp(fileName):  # chinaProxyIp 或 foreignProxyIp
    file = open("./proxyIp/" + fileName + ".txt", 'r')
    ipProxyList = []
    while True:
        temp = file.readline()
        if temp != '':
            print "正在从 ",fileName," 取出一行"
            temp = temp.split("#")[1]
            ipProxyList.append(eval(temp))  # 取出#后面的ip
        else:
            print "从 ",fileName," 取出完毕"
            break
    return ipProxyList


def saveAliveIp(fileName):
    ipProxyList = getProxyIp(fileName)
    newIpProxyList = []
    for i in range(0, len(ipProxyList)):
        if testIp(ipProxyList[i]):  # 测试ip有效，则把它放到新的列表
            newIpProxyList.append(ipProxyList[i])
        time.sleep(1)

    fileIp = open('ip.txt', 'w')
    for ipProxy in newIpProxyList:
        fileIp.write(str(ipProxy) + '\r\n')  # 更新ip.txt
        print "成功更新ip.txt一行"
    fileIp.flush()
    fileIp.close()
    print "ip.txt 更新完成"


def testIp(ipProxy):  # 测试代理是否有效
    proxy_support = urllib2.ProxyHandler(ipProxy)
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    try:
        print "测试 ip 是否有效"
        req = urllib2.urlopen('http://www.baidu.com/', timeout=20)
        req.read()
    except:
        print "此ip无效"
        return False
    return True


def getProxyIpControl():
    flag = 0
    while flag == 0:
        flag = getIpFromYDL()
    saveAliveIp('chinaProxyIp')

getIpFromYDL()
# getProxyIpControl()