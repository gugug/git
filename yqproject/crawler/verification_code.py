#coding=utf-8
__author__ = 'yc'

import urllib
from yqproject.settings import *


def get_image(src):
    """
    保存验证码图片
    :param src: 图片下载地址
    :return:
    """
    u = urllib.urlopen(src)
    data = u.read()
    split_path = src.split('/')
    pic_name = split_path.pop()
    # pic_file = DOC_DIR+'/verification_code/'+str(pic_name)+'.gif' #本文件夹地址
    pic_file = '/media/yc/study/数据挖掘/验证码/'+str(pic_name)+'.gif'  #方便以后用的地址
    print pic_file
    urllib.urlretrieve(src, pic_file)
    return pic_file


# get_image('http://weibo.cn/interface/f/ttt/captcha/show.php?cpt=2_f9c5879ecfcdaebd')