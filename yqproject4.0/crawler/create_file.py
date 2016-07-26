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
        sna_dir = topic_dir.replace('documents','static/sna')
        return topic_dir,sna_dir
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
        folder = create_topic_file(topic)
        total_dir = folder[0] + '/' + str(other_style_time) + '/'
        pic_dir =  folder[1] + '/' + str(other_style_time) + '/'
        short_dir = 'topic' + '/' + str(topic) + '/' + str(other_style_time) + '/'
        if os.path.exists(total_dir):
            print '语料目录已存在'
        else:
            os.makedirs(total_dir)
            print '语料目录创建成功'
        if os.path.exists(pic_dir):
            print 'sna图片目录已存在'
        else:
            os.makedirs(pic_dir)
            print 'sna图片目录创建成功'
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
