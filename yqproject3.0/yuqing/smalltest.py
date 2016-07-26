#coding=utf-8
__author__ = 'yc'
from yqproject.settings import *
import re
# file = open(BASE_DIR+'/static/scripts/lineChart.js','r')
# new_file = open(BASE_DIR+'/static/scripts/linechart.js','w+')
# a=file.readlines()
# xaxis="['1.8','1.9','1.10','1.11','1.12','1.13','1.14','1.15','1.16','1.17','1.18','1.19','1.20','1.21','1.22','1.23','1.24','1.25','1.26','1.27','1.28','1.29','1.30']"
# yaxis=[]
# seris_data = "[12, 13, 10,6,3,5,11, 11, 15, 13, 12, 13, 10,6,3,5]"
# print type(a)
# a[40]=a[40].replace('xaxis',xaxis)
# a[72]=a[72].replace('seris_data',seris_data)
# for i in a:
#     # i=i.replace('\r\n','')
#     new_file.write(i)
#     print i

event = '魏则西之死'
re.compile(event)
path_list = []
for root, dir, file in os.walk('../documents/topic1'):
        if "label_link.xls" in file:
            path = os.path.join(root,'label_link.xls')
            path_list.append(path)

for i in path_list:
    a = re.search(event,i)
    if a is not None:
        print i

print BASE_DIR