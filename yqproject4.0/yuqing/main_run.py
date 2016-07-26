#coding=utf-8
import time

__author__ = 'yc'

import multiprocessing as mul
from network.main import *
from crawler.class_increment import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def auto_run():
    """定时启动获取数据的函数,以后会执行更多自动运行的函数"""
    while True:
        ctime=datetime.datetime.now()
        print '运行时间',ctime
        multi_run()
        time.sleep(7200)  # 单位是秒



def multi_run():
    """
    以多进程形式运行获取数据的函数.
    """
    try:
        inc=Increment()
        rows=inc.get_data('2803301701')
        pool=mul.Pool(processes=2)
        run=[main_network(),main_weibo()]
        for func in run:
                pool.apply_async(func)
        pool.close()
        pool.join()
        print '完成多进程'
    except :
        print 'multiprocessing error'
#
# if __name__ == "__main__":
#     auto_run()