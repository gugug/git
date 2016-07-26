# coding=utf-8
from class_weibo import *
from get_hunter_weibo import *
from get_topic_to_search import *
__author__ = 'gu'

def detection():
    """
    检测器
    猎头传进去检测新事件
    :return:
    """
    account = {
        "人民日报": 2803301701, "新浪新闻": 2028810631, "凤凰周刊": 1267454277,
        "网易新闻客户端": 1974808274, "北京晨报": 1646051850, "头条新闻": 1618051664,
        "人民网": 2286908003, "财经网": 1642088277, "新京报": 1644114654,
        "中国新闻网": 1784473157, "三联生活周刊": 1191965271, "法制晚报": 1644948230,
        "新闻晨报": 1314608344, "中国之声": 1699540307, "中国新闻周刊": 1642512402,
        "澎湃新闻": 5044281310, "中国日报": 1663072851, "北京青年报": 1749990115,
        "新快报": 1652484947, "华西都市报": 1496814565, "凤凰网": 2615417307,
        "FT中文网": 1698233740, "环球时报": 1974576991,
    }
    rand_account = random.sample(account, 2)  # 从 account 中随机获取5个元素，作为一个list返回
    detection_process = []
    for acc in rand_account:
        print "当前猎头：", acc, account[acc]
        save_to_search = SaveTopicToSearch(account[acc])
        s = multiprocessing.Semaphore(2)
        detection_process = multiprocessing.Process(target=save_to_search.save_topic_to_search, args=(1, 2, s))
        detection_process.start()
    detection_process.join()
    print '完成多进程'
