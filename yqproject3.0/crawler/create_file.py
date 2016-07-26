# coding=utf-8
import datetime
import sched

__author__ = 'gu'
import time
from yqproject.settings import *
from crawler.class_save_data import *

s = sched.scheduler(time.time, time.sleep)


def create_topic_file(topic):
    try:
        dir = os.path.join(BASE_DIR, 'documents', 'topic', str(topic))
        #  os.path.join()的功能仅仅是连接的作用，而不能生成
        # print dir
        # if os.path.exists(dir):
        #     pass
        # else:
        #     os.makedirs(dir)
        print dir
        return dir
    except:
        pass


def create_time_file(topic):
    """
    创建txt文档
    :param topic:
    :return:
    """
    try:
        # 获得当前时间
        now = datetime.datetime.now()  # 这是时间数组格式
        # 转换为指定的格式:
        other_style_time = now.strftime("%Y-%m-%d %H:%M:%S")
        a = create_topic_file(topic) + '/' + str(other_style_time) + '/'
        b = topic + '/' + str(topic) + '/' + str(other_style_time) + '/'
        print b
        if os.path.exists(a):
            print '文件已存在'
        else:
            os.makedirs(a)
            print '文件创建成功'
            return b
    except:
        pass

def get_fold_path(topic):
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    path = topic+'/'+str(time)+'/'
    return path

def perform(topic, inc):
    s.enter(inc, 0, perform, (topic, inc,))
    create_time_file(topic)

def my_main(topic, inc):
    s.enter(0, 0, perform, (topic, inc,))
    s.run()


# def create_newtork(topic):
#
# if __name__ == '__main__':
#     # create_topic_file('【#太阳的后裔】')
#     create_time_file("【太阳的龟孙子】")
#
#     # my_main('【太阳的龟孙子】',2)

