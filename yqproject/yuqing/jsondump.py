# coding=utf-8
"""
用于向前端传输json格式的数据
"""
__author__ = 'yc'
import json
import random
import xlrd
from yqproject.settings import *
from crawler.class_increment import *
from crawler.class_event import *
from crawler.class_networkscale import *

def dump_bar():
    """
    :return:柱状图的数据
    """
    data = {}
    return json.dumps(data, separators=(',', ':'))

def dump_time_line():
    data=[]
    eve=Event()
    result = eve.get_topic()
    if len(result) == 0:
        month_list = [4,4,4,4,4,4,4,4]
        day_list = ['1','5','10','20','23','25','27','30']
        event_list = ['科比告别战','山东疫苗案','常州外国语污染事件','日本熊本县地震','网络主播18日起实名认证','东莞坍塌',
                       '泛亚有色涉嫌非法集资','巴萨猝死']
        for i in range(len(month_list)):
            event_dict ={'month':month_list[i],'day':day_list[i],'topic':event_list[i]}
            data.append(event_dict)
    else:
        for j in range(len(result)):
            event_dict = result[j]
            data.append(event_dict) #[{}{}]
    for i in data:
        print 'data',i
    return data
    # return json.dumps(data, separators=(',',':'))

def dump_line():
    """
    :return:折线图的数据
    """
    inc = Increment()
    inc.get_data('111')
    xaxis = str(inc.time_list)
    yaxis = []
    seris_data = str(inc.scale_rate)
    file = open(BASE_DIR+'/static/scripts/lineChart.js','rw')
    new_file = open(BASE_DIR+'/static/scripts/line_chart.js','w+')
    a=file.readlines()
    a[40]=a[40].replace('xaxis',xaxis)
    a[71]=a[71].replace('seris_data',seris_data)
    data={}
    return json.dumps(data, separators=(',', ':'))


def dump_force():
    """
    :return:关系图的数据
    """
    node_list = []
    edge_list = []
    event_id = ''
    # file_name = DOC_DIR + NetworkScale().get_path('topicM_DtDVOsU6Z')
    # file_name = DOC_DIR+'/topic/魏则西之死 谁之过？/2016-05-02 19:30:00/label_link.xls'
    file_name = BASE_DIR+'/network/result/new_label_link.xls'
    data = xlrd.open_workbook(file_name)
    sheet1 = data.sheet_by_index(0)
    sheet2 = data.sheet_by_index(1)
    id_list = sheet1.col_values(0, 1)
    label_list = sheet1.col_values(1, 1)
    from_list = sheet2.col_values(0, 1)
    to_list = sheet2.col_values(1, 1)
    weight_list = sheet2.col_values(2, 1)

    for i in range(0, len(id_list)):
        node_dict = {'id': id_list[i], 'label': label_list[i], 'group': 0, 'value': 1}
        node_list.append(node_dict)
    for i in range(0, len(from_list)):
        edge_dict = {'from': from_list[i], 'to': to_list[i],'weight': weight_list[i]}
        edge_list.append(edge_dict)

    node_data = json.dumps(node_list, separators=(',', ':')) #[{}]
    edge_data = json.dumps(edge_list, separators=(',', ':'))
    # print node_data
    data = [node_data, edge_data]
    return data


def dump_pie():
    """
    :return:饼状图的数据
    """
    data = {}
    return json.dumps(data, separators=(',', ':'))

# print dump_force()[0]
# for i in range(1,5):
