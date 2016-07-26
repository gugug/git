# coding=utf-8
import datetime
import sched

__author__ = 'gu'
import time
from yqproject.settings import *
from crawler.class_save_data import *

s = sched.scheduler(time.time, time.sleep)

def create_topic_file(topic):
    """
    生成话题文件
    :param topic:
    :return:
    """
    try:
        topic_dir = os.path.join(BASE_DIR, 'documents', 'topic', str(topic))
        return topic_dir
    except:
        pass

def create_time_file(topic):
    """
    创建txt文档
    :param topic:
    :return: short_dir
    """
    try:
        now = datetime.datetime.now()
        other_style_time = now.strftime("%Y-%m-%d %H:%M:%S")

        total_dir = create_topic_file(topic) + '/' + str(other_style_time) + '/'

        short_dir = 'topic' + '/' + str(topic) + '/' + str(other_style_time) + '/'
        if os.path.exists(total_dir):
            print '文件已存在'
        else:
            os.makedirs(total_dir)
            print '文件创建成功'
        return short_dir
    except:
        pass

# def get_fold_path(topic):
#     now = datetime.datetime.now()
#     time = now.strftime("%Y-%m-%d %H:%M:%S")
#     path = topic + '/' + str(time) + '/'
#     return path

# def perform(topic, inc):
#     s.enter(inc, 0, perform, (topic, inc,))
#     create_time_file(topic)
#
# def my_main(topic, inc):
#     s.enter(0, 0, perform, (topic, inc,))
#     s.run()
