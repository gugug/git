#coding=utf-8
"""
操作指南:
0.sudo pip install django==1.8.4 如果1.8以下请卸载
  sudo pip install mysql (这句我不确定,因机而定,请百度)
  sudo nano /etc/mysql/my.cnf 按我发的txt修改数据库配置,ctrl+x保存退出
  sudo /etc/init.d/mysql restart 如果fail很可能是配置写错了,从新开来看下
  sudo apt-get install ssh
  登录数据库,按txt给yc授权

1.修改:class_all_id.py:
    def __init__(self):
        self.base_dir='/home/yc/PycharmProjects/dbtest2/sina/results/'
        self.text_dir='/home/yc/PycharmProjects/dbtest2/sina/blogtext/'
        这两个路径改成你们想要的路径
2.城市编号有效范围:1-9,12-20,51-53,大家协调好每人爬一点"
3.在终端下:python manage.py makemigrations
          python manage.py migrate
          python manage.py createsuperuser --创建账户
          设置好账号后
          python manage.py runserver
          开浏览器:http://127.0.0.1/admin 一切都没问题证明ok了
          然后请运行main_mp.py(就是现在这个)

开通他人可以访问的服务器: python manage.py runserver 0.0.0.0:8000
http://本机ip地址:8000 即可访问
"""
__author__ = 'yc'

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","dbtest2.settings")
django.setup()
import multiprocessing as mul
from class_all_id import Uid



if __name__=='__main__':
    # login=Sina()
    # login.login('70705420yc@sina.com','1234567')
    crawler=Sina()
    process1=[]
    lock=mul.Lock()
    #先在terminal下运行python manage.py makemigrations,python manage.py migrate,再n运行此文件,如果不行把下句的#去掉
    #crawler.database()
    uiddd=crawler.getUser(5,10,15,30) #a,b为城市编号范围,c,d粉丝页的页码范围,输出结果为id列表
    for uid in uiddd:
        a=mul.Process(target=crawler.getFans, args=(uid,1,10))
        a.daemon=True
        a.start()
        b=mul.Process(target=crawler.getFollow, args=(uid,1,10))
        b.daemon=True
        b.start()
        # c=mul.Process(target=crawler.getPage, args=(uid,1,10))
        # c.daemon=True
        # c.start()
        process1.append(a)
        process1.append(b)
        # process1.append(c)
        for jc in process1:
            jc.join()
        print '完成多线程'
