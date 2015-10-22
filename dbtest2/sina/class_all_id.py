#coding=utf-8
'''
全部def放一起的py
9.2改动:
1.range改为xrange
2.print的内容改动
3.文档路径改写,方便移植
4.数据库错误捕捉
9.3改动:
1改装为类
2写进程池,目前mp实现了,pool像单进程在跑
'''
__author__ = 'yc', 'gu'

import django,os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","dbtest2.settings")
django.setup()

from dua.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.db import  IntegrityError
from _mysql_exceptions import ProgrammingError
from class_login import *

class Uid(Login):
    def __init__(self):
        Login.__init__(self)
        self.base_dir='/home/gu/PycharmProjects/dbtest2/sina/results/'
        self.text_dir='/home/gu/PycharmProjects/dbtest2/sina/blogtext/'
        self.default_title ="anonymous"
        self.header = {
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/35'}
        # 'cookie':'SUHB=0auQu-VKohQewN; Hm_lvt_16374ac3e05d67d6deb7eae3487c2345=1438853337; gsid_CTandWM=4uNEa18a1iXLheOZzx4XAnLede5; _T_WM=9680670dc09c465d401000970f08a051'}
        # 'cookie':'SUB=_2A254_6A0DeTxGeNI7VER-S3EzD-IHXVYA8B8rDV6PUJbrdAKLUbekW1-zwbkLzaRdvZqxj6DUj5ImWtgBQ..; expires=Sun'
        # ', 18-Oct-2015 08:50:44 GMT; path=/; domain=.weibo.cn; httponly'
        # 'gsid_CTandWM=4uNEa18a1iXLheOZzx4XAnLede5; expires=Sun, 18-Oct-2015 08:50:44 GMT; path=/; domain=.weibo'
        # '.cn; httponly'
        # 'PHPSESSID=f9fda472d39c7edf93bae7a2cd950d7f; path=/'}
        self.user_list=[]

        self.fans_list=[]
        self.gd_fans = []
        self.follow_list = []
        self.gd_follow = []   #以上都是class_all_id里要用的

#程序休眠,避免一次爬太多
    def sleep(self):
        account=self.account[random.randint(0,len(self.account)-1)]
        print account
        self.login(account[0],account[1])
        time.sleep(random.randint(0,5))



    def getUser(self,citystart,cityend,pagestart,pageend): #输入城市编号和页数,返回用户id列表并存入数据库
        print '正在获取用户...'
        same_city =os.path.join(self.base_dir,'user_id.txt')   #存储同城的微博用户Id及name到txt
        city_file=open(same_city,"w+")
        for c in xrange(citystart,cityend):
            self.sleep()
            print '正在输出编号为',c,'的城市'
            for p in xrange(pagestart,pageend):
                print '正在输出第',p,'页的同城用户'
                url = "http://weibo.cn/find/city?province=44&city="+str(c)+"&vt=4&page="+str(p)      # 同城微博用户url
                req = urllib2.Request(url=url,headers=self.header)
                text = urllib2.urlopen(req).read()
                # print 'getUser',text
                user_id = re.compile('</td><td.*?top"><a href.*?vt=4">(.*?)<.*?粉丝(.*?)人&.*?uid=(.*?)&')          # 匹配同城微博用户的id及name
                l = user_id.findall(text)
                if p%5==0:
                    self.sleep()
                if len(l) == 0:
                    print '该账号无法使用'
                    self.sleep()
                    p-=1
                else:
                    for item in l :
                        if int(item[1])>20:
                            # city_file.write(item[2]+"\t"+item[0]+"\n")
                            # self.sleep()
                            self.user_list.append(item[2])
                            try:
                                SinaUser.objects.get(user_id=item[2],user_name=item[0])
                            except ObjectDoesNotExist:
                                try:
                                    SinaUser.objects.create(user_id=item[2],user_name=item[0])
                                except:
                                    print '用户无法存入数据库'
                                    continue

                # self.sleep()
                # try:
                #     ip_changing()
                # except:
                #     pass
        # city_file.close()
        print '获取用户完成,总共有',len(self.user_list),'人'
        return self.user_list                         # 返回同城用户Id的list


#输入想要的粉丝页数,获取粉丝的id和名字并存入数据库,返回广东粉丝列表
    def getFans(self,i,fanspagestart,fanspageend):             # 爬粉丝的id及name,
        print '正在获取粉丝,开始时间:',time.time()
        the_fans_text = os.path.join(self.base_dir,"fans_id.txt")   #存储全部粉丝的Id及name
        # fans_file = open(the_fans_text,"w+")
        gd_fans_txt = os.path.join(self.base_dir,"gd_fans.txt")    #存储过滤后广东粉丝的Id及name
        gd_fans_file = open(gd_fans_txt,"w+")
        # for i in self.user_list:
        print '用户： ',i
        for j in xrange(fanspagestart,fanspageend):
            if j%5==0:
                self.sleep()
            crawler_fans_url = "http://weibo.cn/"+i+"/fans?page="+str(j)           # 第ele个人的第j页粉丝链接
            # print crawler_fans_url
            req_fans= urllib2.Request(url=crawler_fans_url,headers=self.header)
            fans_text = urllib2.urlopen(req_fans).read()
            fans_id = re.compile('<br/>粉丝(.*?)人.*?uid=(.*?)&')     # 匹配粉丝数大于20人的粉丝的id
            fans = fans_id.findall(fans_text)

            if (len(fans)==0):
                print '该账号无法使用'
                self.sleep()
            else:
                for item in fans:
                    if int(item[0])>100:
                        # if int(item[0])/10<fanspageend:
                        #     fanspageend=int(item[0])
                        # print type(item[0])
                        # print item[0] +'粉丝数'
                        # print item[1]
                        # fans_file.write(i+","+item[1]+"\n")                              #没过滤掉的粉丝写入FansFile
                        self.fans_list.append(item[1])

                        fans_home_page_url = "http://weibo.cn/"+item[1]                        # 即将进行判断是否广东的粉丝的链接
                        req_fans_home_page = urllib2.Request(url=fans_home_page_url,headers=self.header)
                        fans_homepage_text = urllib2.urlopen(req_fans_home_page).read()
                        # self.sleep()
                        judge_fans_add = re.compile('<span class="ctt">(.*?)&.*?/广东.*?uid=(.*?)&') # 判断是不是广东,匹配广东匹配成功，返回粉丝id，不成功，则不返回
                        fans_list = judge_fans_add.findall(fans_homepage_text)
                        for k in fans_list:
                            pattern=re.compile('<.*?>')
                            fans_name=re.sub(pattern,'',k[0])
                            print fans_name,"tyty"

                            while fans_list.count(k[1])>1:
                                del fans_list[fans_list.index(k[1])]
                            print k[1]+fans_name+"粉丝"
                            gd_fans_file.write(i+","+k[1]+"\n")        #过滤后的粉丝写入GDFansFile
                            self.user_list.append(k[1]) #把这个人也加入到userlist中
                            try:
                                GDFan.objects.get(user_id=i,gdfans_id=k[1])
                            except ObjectDoesNotExist:
                                try:
                                    GDFan.objects.create(user_id=i,gdfans_id=k[1])
                                    SinaUser.objects.create(user_id=k[1],user_name=fans_name)
                                    # 把该粉丝也写入用户列表的数据库中
                                except : #ProgrammingError:
                                    print '粉丝无法存入数据库'
                                    continue

        # fans_file.close()                                         #没有过滤的粉丝文件关闭
        gd_fans_file.close()                                       #过滤后的粉丝文件关闭
        print '储存粉丝完成'
        return self.user_list      # 返回过滤后只剩广东的粉丝ID

#输入想要的关注页数,获取关注的id和名字并存入数据库,返回广东关注列表
    def getFollow(self,i,followpagestart,followpageend):
        print '正在获取关注,开始时间:',time.time()
        # the_follow_text = os.path.join(self.base_dir,"follow_id.txt")     #存储全部关注的Id及name
        # follow_file = open(the_follow_text,"w")
        only_gd_follow = os.path.join(self.base_dir,"gd_follow.txt")     #存储过滤后广东关注的Id及name
        gd_follow_file = open(only_gd_follow,"w")

        # for i in self.user_list:
        print '用户： ',i
        for j in xrange(followpagestart,followpageend):
            if j%5==0:
                self.sleep()
            crawler_follow_url = "http://weibo.cn/"+i+"/follow?page="+str(j)          # 第ele个人的第j页关注链接
            reqfollow= urllib2.Request(url=crawler_follow_url,headers=self.header)
            follows_text = urllib2.urlopen(reqfollow).read()
            follows_id = re.compile('<br/>粉丝(.*?)人.*?uid=(\d\d+)&')          # 匹配没过滤粉丝数大于20的关注的人的id
            follows = follows_id.findall(follows_text)
            if len(follows)==0:
                print '该账号无法使用'
                self.sleep()
                j-=1
            else:
                for item in follows:
                    if int(item[0])>100:
                        # print item[0]+'粉丝数'
                        # print item[1]
                        # follow_file.write(i+"\t"+item[1]+"\n")                               #没过滤的关注写入FollowFile
                        self.follow_list.append(item[1])
                        follows_homepage_url = "http://weibo.cn/"+item[1]                       # 即将进行判断是否广东的关注链接
                        req_follows_homepage = urllib2.Request(url=follows_homepage_url,headers=self.header)
                        follows_homepage_text = urllib2.urlopen(req_follows_homepage).read()
                        # self.sleep()

                        judge_follows_add = re.compile('<span class="ctt">(.*?)&.*?/广东.*?uid=(.*?)&') # 判断是不是广东,匹配广东匹配成功，返回粉丝id,不成功,则不返回
                        follows_list = judge_follows_add.findall(follows_homepage_text)

                        for k in follows_list:
                            pattern=re.compile('<.*?>')
                            follows_name=re.sub(pattern,'',k[0])
                            while follows_list.count(k[1])>1:
                                    del follows_list[follows_list.index(k[1])]
                            print k[1]+follows_name+"关注"
                            gd_follow_file.write(i+"\t"+k[1]+"\n")          #过滤后的关注写入GDFollowFile
                            self.user_list.append(k[1])  #把这个人也加入到userlist中
                            try:
                                GDFollow.objects.get(user_id=i,gdfollows_id=k[1])
                            except ObjectDoesNotExist:
                                try:
                                    GDFollow.objects.create(user_id=i,gdfollows_id=k[1])
                                    SinaUser.objects.create(user_id=k[1],user_name=follows_name) #把该关注也加入用户列表的数据库
                                except: #ProgrammingError:
                                    print '关注无法存入数据库'
                                    continue
                                # except IntegrityError:
                                #     pass
        # follow_file.close()                                          #没有过滤的关注文件关闭
        gd_follow_file.close()                                        #过滤后的关注文件关闭
        print '储存关注完成'
        return self.user_list                                            # 返回过滤后的关注id

