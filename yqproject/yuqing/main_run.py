#coding=utf-8
__author__ = 'yc'

import multiprocessing as mul

from crawler.class_increment import *
from crawler.class_weibo import *

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
        pool=mul.Pool(processes=3)
        run=[main_weibo(),main_network()]
        for func in run:
                pool.apply_async(func)
        pool.close()
        pool.join()
        print '获取增量数据完成'
    except :
        print 'multiprocessing error'

if __name__ == "__main__":
    auto_run()