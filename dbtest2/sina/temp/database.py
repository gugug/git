#coding=utf-8
__author__ = 'yc'

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","dbtest2.settings")
django.setup()
import MySQLdb
# a=uni.getUser(1,2,1,2)
# b=uid.getPage(a,1,2)
# c=ff.getFans(a,1,2)
# d=ff.getFollow(a,1,2)
# a=('1','2','3')
# b=('4','5','6')
# c=('7','8','9')
# a=uni.getUser(1,2,1,2)
# b=uid.getPage(a,1,2)
# c=w.tupling(a,b[0],b[1])

# cc=chardet.detect(c[0][0][1])
# print cc['encoding']
# print type(c[0][0][0])  #type:str, encoding utf-8  a str.decode('gbk')=u'\...', a unicode.encode('gbk')=\xE80...
def store_weibo():
    sqli="insert into test4 values (%s,%s,%s)"

    conn= MySQLdb.connect(
            host='127.0.0.1',
            port = 3306,
            user='root',
            passwd='uliuli520',
            db ='sina',
            charset='utf8',
    )
    cur = conn.cursor()

     #创建数据表
    cur.execute('create table wbtest2(uid varchar (20),times varchar (200),weibo text (500))ENGINE=INNODB DEFAULT CHARSET=utf8;')



     # 插入一条数据
    # for i in mix:
    #     for ii in i:
    #         print ii
    ii=('a','a','a')
    cur.execute(sqli,ii)
    # sql='select * from test4' #
    # result=cur.execute(sql)  #
    # for i in cur.fetchall(): #返回全部记录,这句要先有上面带#的两句
    #     print 'i',i[0]
    # cur.fetchone() #返回一条记录
     #插入多条数据,a,b,c为元组
     # cur.executemany(sqli,[a,b,c])            8\xe6\x9c\x8805\xe6\x97\xa
     #插入数据,暂时无法使用
     # cur.execute("load data local infile '/home/yc/PycharmProjects/sina/results/gd_fans.txt' into table test2")

    cur.close()
    conn.commit()
    conn.close()

# cc=[[('a','b','c'),('1','2','3'),('b','s','d')]]
# store_weibo(cc)
a=store_weibo()