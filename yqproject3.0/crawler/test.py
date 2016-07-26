# coding=utf-8
# # import random
# # import re
# # from time import sleep
# #
# # __author__ = 'yc'
# # class A():
# #
# #     afore_all_uid = {}
# #     def __init__(self):
# #         self.a = []
# #         self.b = [1,4,5,6,7,2,3,4,5]
# #         self.afore_all = []
# #
# #
# #     def test(self):
# #         c = [5,6,7,8,9]
# #         self.b = list(set(self.b + c))
# #         print self.b
# #
# #     def tt(self):
# #         t1 = [1,2,3,4,5]
# #         t2 = [2,3,4,5,5]
# #         t3 = [4,5,6,7,5]
# #         return t1,t2,t3
# #
# #     def save_afore(self):
# #
# #         t = self.tt()
# #         z = zip(t[0],t[1],t[2])
# #         self.afore_all_uid.setdefault(0,z)
# #         self.afore_all_uid.setdefault(1,z)
# #         print type(z)
# #         # for i in z:
# #             # print i
# #             # if i not in self.afore_all_uid.values():
# #                 # print 'ss'
# #                 # self.afore_all_uid.setdefault(0,[]) .append(i)
# #         print len(self.afore_all_uid)
# #         print self.afore_all_uid
# #         # print 'sfsas'
# #         # for uid,list in self.afore_all_uid.items():
# #             # for tuple in list:
# #                 # print uid,tuple
# #     def update(self):
# #         print "更新"
# #
# #     def run(self):
# #         if self.afore_all_uid:
# #             self.update()
# #         else:
# #             print "无"
# #
# #         for i in range(5):
# #             a = A()
# #             print "changdu",len(self.afore_all_uid)
# #             a.save_afore()
# #
# #     def auto_run(self):
# #         while True:
# #             self.run()
# #             sleep(2)
# #             print "睡醒"
# #
# # A().auto_run()
# #
# #
# #
# #
# #
# #
# #
# # # # print t
# # # print '博文',t[2]
# # # z = zip(t[0],t[1],t[2])
# # # print z
# # # print len(z)
# # # for i in range(len(z)):
# # #     print z[i]
# #
# # # A().test()
# #         # e = []
# #
# #         # for i in range(3):
# #         #     print self.a
# #         #
# #         #     for j in c:
# #         #         if j not in self.a:
# #         #             print '不在'
# #         #             e.append(j)
# #         #         else:
# #         #             print "zai"
# #         #     self.a += e
# #         # print self.a
# #
# # # A().test()
# # # print len(c)
# # # for i in range(0,len(c)):
# # #     print c[i][0]
# # # result_num = [1]
# # # if result_num:
# # #     result_num.append(1)
# # # else:
# # #     result_num.append(2)
# # #
# # # print result_num
# #
# #
# # # blogstr ='【年轻人广场玩“彩虹跑” 满地粉末愁坏清洁工[smile]】近日，一群青年在成都萃锦西路的公共广场开展“彩虹跑”活动，留下一片狼藉，地面遍布彩色粉末，风一吹便扬起粉尘。如何清理难坏清洁工。主办方称粉末是染色玉米粉，有人清理，但直到清洁工清理完毕，也未见商家工作人员来清扫。年轻人广场上玩“彩虹跑” 满地粉末愁怀清洁工 [组图共2张]'
# # #
# # # topic_patternts = re.compile('#(.*?)# |【(.*?)】')
# # # topic = topic_patternts.findall(blogstr)
# # # print len(topic)
# # # if len(topic):
# # #
# # #     topic = [topic[0][0]+topic[0][1]]
# # #
# # #     print 'ss',topic[0]
# # #     topic_clean_pattern = re.compile('(\[.*?])')
# # #     t = topic_clean_pattern.findall(topic[0])
# # #     print t
# # #     topic = [re.sub(topic_clean_pattern,'',topic[0])]
# # #     print topic[0]
# #
# #
# #
# #
# # #
# # # t1 = [1,2,3,4,5]
# # # t2 = [2,3,4,5,5]
# # # t3 = [4,5,6,7,5]
# # #
# # # t4 = list(set(t1+t2))
# # # print t1
# # # print t2
# # # print type(t4)
# # # print t4
# #
# # account = {
# #     "人民日报": 2803301701, "新浪新闻": 2028810631, "凤凰周刊": 1267454277,
# # #     "网易新闻客户端": 1974808274, "北京晨报": 1646051850,
# # #     "头条新闻": 1618051664, "人民网": 2286908003,
# # #     "财经网": 1642088277, "新京报": 1644114654, "环球时报": 1974576991,
# # #     "中国新闻网": 1784473157, "三联生活周刊": 1191965271, "法制晚报": 1644948230,
# # #     "新闻晨报": 1314608344, "中国之声": 1699540307, "中国新闻周刊": 1642512402,
# # #     "澎湃新闻": 5044281310, "中国日报": 1663072851, "北京青年报": 1749990115,
# # #     "新快报": 1652484947, "华西都市报": 1496814565, "凤凰网": 2615417307,
# # #     "FT中文网": 1698233740,
# # # }
# # # a = random.sample(account,5)
# # # for i in a:
# # #     print i
# # # print type(a)
# # # print a[0]
# # # print account[a[0]]
# # from time import sleep
# #
# # #
# # class A:
# #     a = []
# #     # def __init__(self):
# #
# #     def printr(self):
# #
# #         A.a.append(1)
# #         A()
# #         A()
# #
# # def b():
# #     while True:
# #         AA = A()
# #         AA.printr()
# #         print A.a
# # b()
#
# #
# #
# # a = [1,3,5]
# # if a:
# #     print 'dd'
# # else:
# #     print 'f'
# #
# # n = '\xe9\x9c\x87\xe6\x83\x8a\xef\xbc\x81\xe5\xa4\xa7\xe6\xad\xa5\xe8\xb7\x91\xe4\xbc\xa4\xe8\x86\x9d\xe7\x9b\x96'
# # print n
# #
# # a = [[('89\xe5\x8e\x98\xe7\xb1\xb3\xe9\xab\x98\xe2\x80\x9c\xe7\x93\xb7\xe5\xa8\x83\xe5\xa8\x83\xe2\x80\x9d \xe5\xbd\x93\xe5\xa6\x88', '\xe5\x8e\x98\xe7\xb1\xb3 89 \xe7\x93\xb7\xe5\xa8\x83\xe5\xa8\x83 \xe8\x83\xa1\xe9\x99\x86 \xe5\xa6\x88 ', 'M_DurY6s5py'), ('\xe5\xa4\xab\xe5\xa6\xbb\xe5\xb8\xa6\xe7\xbe\xbd\xe7\xbb\x92\xe6\x9c\x8d\xe6\xb8\xb8\xe9\x9f\xa9\xe5\x9b\xbd\xe8\xa2\xab\xe9\x81\xa3\xe8\xbf\x94 \xe9\x9f\xa9\xe6\x96\xb9\xef\xbc\x9a\xe6\x9c\x89\xe9\x9d\x9e\xe6\xb3\x95\xe6\xbb\x9e\xe7\x95\x99\xe5\xab\x8c\xe7\x96\x91', '\xe7\xbe\xbd\xe7\xbb\x92\xe6\x9c\x8d \xe9\x9f\xa9\xe6\x96\xb9 \xe5\xa4\xab\xe5\xa6\xbb \xe9\x9f\xa9\xe5\x9b\xbd \xe6\xbb\x9e\xe7\x95\x99 ', 'M_DuqVa8HUO'), ('\xe5\xae\x89\xe5\xbe\xbd\xe5\xb8\x88\xe5\xa4\xa7\xe6\x8e\xa8\xe5\x87\xba\xe2\x80\x9c\xe6\x96\x87\xe6\x98\x8e\xe7\x94\xa8\xe8\xaf\xad\xe7\x89\xb9\xe4\xbb\xb7\xe8\x8f\x9c\xe2\x80\x9d\xef\xbc\x9a\xe6\x89\x93\xe8\x8f\x9c\xe8\xaf\xb4\xe2\x80\x9c\xe9\x98\xbf\xe5\xa7\xa8\xe6\x82\xa8\xe5\xa5\xbd\xe2\x80\x9d\xe6\x89\x935\xe6\x8a\x98', '\xe8\x8f\x9c \xe7\x89\xb9\xe4\xbb\xb7 \xe9\x98\xbf\xe5\xa7\xa8 \xe8\xaf\xb4 \xe5\xae\x89\xe5\xbe\xbd\xe5\xb8\x88\xe8\x8c\x83\xe5\xa4\xa7\xe5\xad\xa6 ', 'M_DuqgznLfs'), ('\xe8\x8a\x92\xe6\x9e\x9c\xe5\x8d\x83\xe5\xb1\x82', '\xe6\xa6\xb4\xe8\x8e\xb2 \xe8\x8a\x92\xe6\x9e\x9c \xe5\x8d\x83\xe5\xb1\x82 \xe6\x95\x99\xe7\xa8\x8b \xe9\xa6\x8b\xe5\x98\xb4 ', 'M_Durbp9jed'), ('\xe5\xb9\xbf\xe4\xb8\x9c\xe7\x9c\x81\xe4\xba\xba\xe6\xb0\x91\xe5\x8c\xbb\xe9\x99\xa2\xe5\x8f\xa3\xe8\x85\x94\xe7\xa7\x91\xe4\xb8\x80\xe5\x8c\xbb\xe7\x94\x9f\xe8\xa2\xab\xe7\xa0\x8d\xe8\x87\xb3\xe7\x94\x9f\xe5\x91\xbd\xe5\x9e\x82\xe5\x8d\xb1', '\xe7\xa0\x8d 5 \xe9\x99\x88\xe4\xbb\xb2\xe4\xbc\x9f \xe5\xb9\xbf\xe4\xb8\x9c\xe7\x9c\x81 \xe5\x8c\xbb\xe9\x99\xa2 ', 'M_Duq546vll'), ('\xe7\x94\xb7\xe5\xad\x90\xe7\xbb\x99\xe5\xa5\xb3\xe5\x8f\x8b\xe7\x88\xb1\xe8\xbd\xa6\xe5\xbd\xa9\xe5\x96\xb7\xe2\x80\x9cLOVE\xe2\x80\x9d\xe6\xb1\x82\xe5\xa9\x9a \xe6\x83\xb9\xe6\x9d\xa5\xe6\x8e\x8c\xe6\x8e\xb4', '\xe7\x94\xb7\xe5\xad\x90 \xe5\xa5\xb3\xe5\x8f\x8b \xe6\xb1\x82\xe5\xa9\x9a LOVE \xe5\xbd\xa9\xe5\x96\xb7 ', 'M_DuqwO8XHA'), ('11\xe5\xb2\x81\xe5\xa5\xb3\xe5\xad\xa9\xe6\x8a\xa5\xe8\xad\xa6\xe8\xa6\x81\xe6\xb1\x82\xe2\x80\x9c\xe8\xbe\x9e\xe9\x80\x80\xe2\x80\x9d\xe7\x88\xb6\xe4\xba\xb2\xef\xbc\x9a\xe5\x8f\xaa\xe7\x88\xb1\xe6\x89\x93\xe9\xba\xbb\xe5\xb0\x86\xef\xbc\x8c\xe7\xbb\x8f\xe5\xb8\xb8\xe4\xb8\x8d\xe5\x9b\x9e\xe5\xae\xb6', '\xe6\x8a\xa5\xe8\xad\xa6 \xe7\x88\xb6\xe4\xba\xb2 \xe6\x89\x93\xe9\xba\xbb\xe5\xb0\x86 \xe5\xa5\xb3\xe5\xad\xa9 \xe8\xbe\x9e\xe9\x80\x80 ', 'M_DuqN2yZYH')]]
# # print a[0]
# # for i in a[0]:
# #     for j in i:
# #         print "ss",j
# #
# #
# # dicta = {1:[(1,2,3)]}
# # for i, j in dicta.items():
# #     print i, j
# # dicta.setdefault(2,[(2,4,5)])
# # if 2 not in dicta.keys():
# #     dicta.setdefault(2,[(2,3,5,5,7)])
# # else:
# #     for i in dicta[2]:
# #         dicta.setdefault(2).append([(2,3,5,5,7)])
# #
# # print dicta.values()
# # print len(dicta)
# # a = list((1,2,3))
# # b = list((2,3,4))
# # # print a+b
# # C = '\xe8\xbf\x99\xe6\xa0\xb7\xe7\x9a\x84\xe2\x80\x9c\xe5\xbe\xae\xe6\x95\xb4\xe5\xbd\xa2\xe2\x80\x9d\xe4\xbd\xa0\xe6\x95\xa2\xe5\x81\x9a\xe5\x90\x97\xef\xbc\x9f/2016-05-07 22:04:58/uid=[1191965271].txt'
# # print C
# #
# # n = [('\xe8\xa1\x80\xe7\xb3\x96\xe9\xab\x98\xe8\xaf\x95\xe8\xaf\x95\xe7\x94\xa8\xe8\x8c\xaf\xe8\x8b\x93\xe7\xb2\x89\xe8\x92\xb8\xe9\xa6\x92\xe5\xa4\xb4', '\xe8\x8c\xaf\xe8\x8b\x93 \xe9\xa6\x92\xe5\xa4\xb4 \xe8\xa1\x80\xe7\xb3\x96\xe9\xab\x98 \xe5\x81\xa5\xe8\x84\xbe \xe4\xb8\xbb\xe9\xa3\x9f ', 'M_DusMQgJZt'), ('\xe4\xbd\x8f\xe6\x88\xbf\xe6\x94\xb9\xe9\x80\xa0\xe5\x90\x8e\xe5\x8f\xaf\xe6\x8c\x89\xe9\x97\xb4\xe5\x87\xba\xe7\xa7\x9f', '\xe4\xbd\x8f\xe6\x88\xbf \xe6\x94\xb9\xe9\x80\xa0 \xe5\x87\xba\xe7\xa7\x9f \xe5\x90\x8e \xe9\x97\xb4 ', 'M_DuorJkdin'), ('\xe5\x85\xa8\xe6\xb0\x91\xe5\x97\xa8\xe6\xad\x8c\xe2\x80\x94\xe2\x80\x94\xe3\x80\x8a\xe6\x88\x91\xe6\x83\xb3\xe5\x92\x8c\xe4\xbd\xa0\xe5\x94\xb1\xe3\x80\x8b\xe4\xbb\x8a\xe6\x99\x9a\xe5\xbc\x80\xe6\x92\xad', '\xe5\x94\xb1 \xe5\x85\xa8\xe6\xb0\x91 \xe7\xbb\xbc\xe8\x89\xba \xe5\xbc\x80\xe6\x92\xad \xe6\x83\xb3 ', 'M_DurBMoh6d'), ('\xe8\xb6\x8a\xe5\x8d\x97\xe6\x9c\xba\xe5\x9c\xba\xe6\x89\xbf\xe8\xae\xa4\xe4\xbf\x9d\xe5\xae\x89\xe6\x89\x93\xe4\xb8\xad\xe5\x9b\xbd\xe6\xb8\xb8\xe5\xae\xa2', '\xe4\xb8\xad\xe5\x9b\xbd \xe8\xb6\x8a\xe5\x8d\x97 \xe6\xb8\xb8\xe5\xae\xa2 \xe4\xbf\x9d\xe5\xae\x89 \xe5\xb0\x8f\xe8\xb4\xb9 ', 'M_DupeQq14O'), ('\xe5\xa4\x9a\xe7\xa7\x8d\xe5\xb8\xb8\xe8\xa7\x81\xe6\xad\xa2\xe5\x92\xb3\xe8\x8d\xaf\xe8\xa2\xab\xe6\xa3\x80\xe5\x87\xba\xe7\xa1\xab\xe7\xa3\xba', '\xe7\xa1\xab\xe7\xa3\xba \xe6\xb5\x99\xe8\xb4\x9d \xe9\x9b\x86\xe5\x9b\xa2 \xe6\xa3\x80\xe6\xb5\x8b \xe8\x8d\xaf ', 'M_DuoPGcjT4'), ('\xe3\x80\x8a\xe7\xbe\x8e\xe5\x9b\xbd\xe9\x98\x9f\xe9\x95\xbf3\xe3\x80\x8b\xe6\x8b\xaf\xe6\x95\x91\xe4\xbd\x8e\xe8\xbf\xb7\xe5\xbd\xb1\xe5\xb8\x82', '\xe7\x94\xb5\xe5\xbd\xb1 \xe6\xbc\xab\xe5\xa8\x81 \xe5\xbd\xb1\xe5\xb8\x82 \xe9\x98\x9f\xe9\x95\xbf \xe7\xbe\x8e\xe5\x9b\xbd ', 'M_DupGrf83P'), ('\xe5\xbc\xa0\xe5\xa4\xa7\xe5\x8d\x83\xe5\x8a\x9b\xe4\xbd\x9c\xe4\xba\xae\xe7\x9b\xb8\xe5\x8d\x8e\xe8\xbe\xb0\xe6\x98\xa5\xe6\x8b\x8d', '\xe5\x8d\x8e\xe8\xbe\xb0\xe6\x98\xa5 \xe5\xbc\xa0\xe5\xa4\xa7\xe5\x8d\x83 \xe5\x8c\x97\xe4\xba\xac \xe4\xba\xae\xe7\x9b\xb8 \xe5\x8a\x9b\xe4\xbd\x9c ', 'M_DuqqIvTcS'), ('2016\xe5\xa4\xa9\xe6\x81\x92\xe2\x80\xa2\xe4\xb9\x90\xe8\xb7\x91\xe6\x98\x8e\xe5\xa4\xa9\xe5\x9c\xa8\xe6\x88\xbf\xe5\xb1\xb1\xe5\x8c\xba\xe5\xb0\x8f\xe6\xb8\x85\xe6\xb2\xb3\xe5\xbc\x80\xe8\xb7\x91', '\xe8\xb7\x91 \xe5\xb0\x8f\xe6\xb8\x85\xe6\xb2\xb3 \xe6\x88\xbf\xe5\xb1\xb1\xe5\x8c\xba \xe5\xa4\xa9\xe6\x81\x92 \xe5\x8c\x97\xe4\xba\xac ', 'M_DurCeaAL7'), ('\xe5\xb1\x85\xe6\xb0\x91\xe5\x8c\xbb\xe4\xbf\x9d\xe8\xb4\xa2\xe6\x94\xbf\xe8\xa1\xa5\xe5\x8a\xa9\xe5\x86\x8d\xe6\x8f\x90\xe9\xab\x9840\xe5\x85\x83', '\xe8\xb4\xa2\xe6\x94\xbf \xe8\xa1\xa5\xe5\x8a\xa9 \xe5\x85\x83 \xe8\xb5\x84\xe9\x87\x91 \xe5\xb1\x85\xe6\xb0\x91 ', 'M_DuqP4rusC')]
# # m =('\xe8\xa1\x80\xe7\xb3\x96\xe9\xab\x98\xe8\xaf\x95\xe8\xaf\x95\xe7\x94\xa8\xe8\x8c\xaf\xe8\x8b\x93\xe7\xb2\x89\xe8\x92\xb8\xe9\xa6\x92\xe5\xa4\xb4', '\xe8\x8c\xaf\xe8\x8b\x93 \xe9\xa6\x92\xe5\xa4\xb4 \xe8\xa1\x80\xe7\xb3\x96\xe9\xab\x98 \xe5\x81\xa5\xe8\x84\xbe \xe4\xb8\xbb\xe9\xa3\x9f ', 'M_DusMQgJZt')
# # for i in n:
# #     print i
# #     print i[0],i[1],i[2]
#
# from multiprocessing import Manager
# import multiprocessing
# import os
# from time import sleep
# import time
# import urllib2
#
#
# class MUL():
#     manager = Manager()
#     vip_list = []
#     vip_list = manager.list()
#     vip_dict={}
#     vip_dict=manager.dict()
#     def __init__(self,id):
#         a= 0
#     def testFunc(self,cc):
#         add = []
#         for i in range(2):
#             self.add(cc)
#
#             # m = MUL(i)
#         #     add = multiprocessing.Process(target=m.add, args=(cc,))
#         #     add.start()
#         # add.join()
#
#         print 'process id:', os.getpid(),MUL.vip_dict
#         self.test()
#
#     def add(self,cc):
#         MUL.vip_list.append(cc)
#         MUL.vip_dict.setdefault(cc,cc)
#         b = [2,3,4]
#         MUL.vip_list = list(set(MUL.vip_list + b))
#         print "ff", MUL.vip_list
#
#     def test(self):
#         # print MUL.vip_dict
#         print MUL.vip_list
# print time.time()
#
# if __name__ == '__main__':
#     start = time.time()
#     # t = []
#     for ll in range(10):
#         mul = MUL(ll)
#         mul.testFunc(ll)
#
#     #     t = multiprocessing.Process(target=mul.testFunc, args=(ll,))
#     #     t.start()
#     # t.join()
#     #     t.daemon = True
#     #     threads.append(t)
#     #
#     # for i in range(len(threads)):
#     #     threads[i].start()
#     #
#     # for j in range(len(threads)):
#     #     threads[j].join()
#
#     print "------------------------"
#     print 'process id:', os.getpid()
#     print mul.vip_list
#     print time.time() - start
#
#
# # a.append(1)
# # print a
#
# # from multiprocessing import Process, Manager
# # import os
# #
# # manager = Manager()
# # sum = manager.Value('tmp', 0)
# #
# # def testFunc(cc):
# #     sum.value += cc
# #
# # if __name__ == '__main__':
# #     threads = []
# #
# #     for ll in range(100):
# #         t = Process(target=testFunc, args=(1,))
# #         t.daemon = True
# #         threads.append(t)
# #
# #     for i in range(len(threads)):
# #         threads[i].start()
# #
# #     for j in range(len(threads)):
# #         threads[j].join()
# #
# #     print "------------------------"
# #     print 'process id:', os.getpid()
# #     print sum.value
#
# # while True:
# #     MUL(1).testFunc(2)
# #     sleep(2)
# #     print "睡醒"
#
#
# # a = '/n/%E4%BB%99%E5%89%91%E6%8E%A2%E4%BA%91?vt=4'
# # b = urllib2.quote(a)
# # print b
#

import urllib
import time

a = "/n/%E4%BB%99%E5%89%91%E6%8E%A2%E4%BA%91?vt=4"
# a = '/n/%E8%BD%A8%E9%81%93%E5%90%9B%E8%BD%A8%E7%88%B6%E6%A8%A1%E5%BC%8FMK1%E5%9E%8B?vt=4'
print urllib.unquote(a).decode('utf-8', 'replace')

def write_search_result(dir_file, list_result):
    txt_file = open(dir_file, 'a+')
    for i in list_result:
        txt_file.write(str(i) + '\n')
    txt_file.write('\n')
    txt_file.close()
    print 'done'

a = [1,2,3,5,6,7,8,9]
b = ['asd','adsf','wett']

start = time.time()
dirfile = 'file.txt'
write_search_result(dirfile, a)
write_search_result(dirfile,b)
end1 = time.time() - start
print end1

start1 = time.time()
file = open('file1.txt','a+')
for i in a:
    file.write(str(i) + '\n')
file.write('\n')
for j in b:
    file.write(str(j) + '\n')
file.write('\n')
file.close()
end2 = time.time() - start1
print end2
print end1 / end2
