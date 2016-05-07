# coding=utf-8
import re
from time import sleep

__author__ = 'yc'
class A():
    def __init__(self):
        self.a = []
        self.b = [1,4,5,6,7,2,3,4,5]
        self.afore_all = []
        self.afore_all_uid = {}


    def test(self):
        c = [5,6,7,8,9]
        self.b = list(set(self.b + c))
        print self.b

    def tt(self):
        t1 = [1,2,3,4,5]
        t2 = [2,3,4,5,5]
        t3 = [4,5,6,7,5]
        return t1,t2,t3

    def save_afore(self):

        t = self.tt()
        z = zip(t[0],t[1],t[2])
        self.afore_all_uid.setdefault(0,z)
        self.afore_all_uid.setdefault(1,z)
        print type(z)
        for i in z:
            print i
            if i not in self.afore_all_uid.values():
                print 'ss'
                # self.afore_all_uid.setdefault(0,[]) .append(i)
        print len(self.afore_all_uid)
        print self.afore_all_uid
        print 'sfsas'
        for uid,list in self.afore_all_uid.items():
            for tuple in list:
                print uid,tuple

    def auto_run(self):
        # while True:
            self.save_afore()
            # sleep(2)
            # print "睡醒"





a = A()
t = a.auto_run()
# # print t
# print '博文',t[2]
# z = zip(t[0],t[1],t[2])
# print z
# print len(z)
# for i in range(len(z)):
#     print z[i]

# A().test()
        # e = []

        # for i in range(3):
        #     print self.a
        #
        #     for j in c:
        #         if j not in self.a:
        #             print '不在'
        #             e.append(j)
        #         else:
        #             print "zai"
        #     self.a += e
        # print self.a

# A().test()
# print len(c)
# for i in range(0,len(c)):
#     print c[i][0]
# result_num = [1]
# if result_num:
#     result_num.append(1)
# else:
#     result_num.append(2)
#
# print result_num


# blogstr ='【年轻人广场玩“彩虹跑” 满地粉末愁坏清洁工[smile]】近日，一群青年在成都萃锦西路的公共广场开展“彩虹跑”活动，留下一片狼藉，地面遍布彩色粉末，风一吹便扬起粉尘。如何清理难坏清洁工。主办方称粉末是染色玉米粉，有人清理，但直到清洁工清理完毕，也未见商家工作人员来清扫。年轻人广场上玩“彩虹跑” 满地粉末愁怀清洁工 [组图共2张]'
#
# topic_patternts = re.compile('#(.*?)# |【(.*?)】')
# topic = topic_patternts.findall(blogstr)
# print len(topic)
# if len(topic):
#
#     topic = [topic[0][0]+topic[0][1]]
#
#     print 'ss',topic[0]
#     topic_clean_pattern = re.compile('(\[.*?])')
#     t = topic_clean_pattern.findall(topic[0])
#     print t
#     topic = [re.sub(topic_clean_pattern,'',topic[0])]
#     print topic[0]




#
# t1 = [1,2,3,4,5]
# t2 = [2,3,4,5,5]
# t3 = [4,5,6,7,5]
#
# t4 = list(set(t1+t2))
# print t1
# print t2
# print type(t4)
# print t4