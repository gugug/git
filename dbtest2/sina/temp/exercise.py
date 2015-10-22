#coding=utf-8
import re
import multiprocessing as m
import time,random,chardet
# a = u"这是个中文a"
# b = re.compile(u"这(.*?)文")
# c = b.findall(a)
# for i in  c:
#     print i
#
# f=[14671947, 10762310, 7742662, 3503992, 4041042, 4680452, 2585314, 5866356, 2280076, 5648976]
# print  type(7742662)
#
#
# tu=[(u'14672940', u'uid=1644395354'), (u'10762724', u'uid=1742566624')]
# for item in tu:
#     print "item",item[0]
#     print "omg",item[1]
#     # for ele in item:
#     #     print "ele",ele
#
# kfjlksdj=str(i for i in range(1,10))
#
# print "a,",type(kfjlksdj)
# t=()
# a=[1,2]
# b=[1,2]
# c=[]
# for i in range(len(a)):
#     t=(a[i],b[i])
#     c.append(t)
# print c

# user1 = ('a','b','c')
# user2 = ('d','e','f')
# user = (user1,user2)
# # userr=(user2,user1)
# # userrr=(user,userr)
# print user[0][0]
def aaa(l):
    a=[[(l,'b','c'),('d','e','f')]]
    b=['d','e','f']
    q.put(a)
    return a,b

def bbb(a,b):
    c=a+b
    return c

def ccc(x,a,b,c):
    x.put(a,b,c)
    return a,b,c

def offer(queue):
    print 'sjldsfjlsdjf'
    queue.put(aaa(l))

if __name__ == '__main__':
    # l='l'
    # q = m.Queue(3)
    # a=m.Queue()
    # p = m.Process(target=offer, args=(q,))
    # # y=m.Process(target=ccc,args=(a,1,2,'3'))
    # # y.start()
    # p.start()
    # for i in range(2):
    #     print q.get()
    # print time.strftime('%m'+'月'+'%d'+'日',time.localtime())
    # print time.gmtime()
    # print time.localtime()
    # for i in range (100):
    #     k= time.clock()
    #
    # i=1
    # while i<3:
    #     print i
    #     i+=1
    # for i in range(1,10):
    #     print str(float(int(random.uniform(1,5))))
    print type(time.strftime('%m'+'月'+'%d'+'日',time.localtime()))
    text=u'今天  sdflsjflsjflsdjfl'
    today=re.compile(u'今天')

    find=re.findall(today,text)
    print 'find',find
    # text=text.encode('gbk','ignore')
    # print '5', type(text)
    t=time.strftime('%m'+'月'+'%d'+'日',time.localtime())
    t=t.decode('utf-8')
    print type(t)
    wbtime=re.sub(today,t,text)
    print '2',wbtime #utf-8
    # print '4',chardet.detect(wbtime)['encoding']
    # wbtime=wbtime.decode('gbk','ignore')
    print '3',wbtime
