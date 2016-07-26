# coding=utf-8
#        ┏┓　　　┏┓+ +
# 　　　┏┛┻━━━┛┻┓ + +
# 　　　┃　　　　　　　┃ 　
# 　　　┃　　　━　　　┃ ++ + + +
# 　　 ████━████ ┃+
# 　　　┃　　　　　　　┃ +
# 　　　┃　　　┻　　　┃
# 　　　┃　　　　　　　┃ + +
# 　　　┗━┓　　　┏━┛
# 　　　　　┃　　　┃　　　　　　　　　　　
# 　　　　　┃　　　┃ + + + +
# 　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
# 　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
# 　　　　　┃　　　┃
# 　　　　　┃　　　┃　　+　　　　　　　　　
# 　　　　　┃　 　　┗━━━┓ + +
# 　　　　　┃ 　　　　　　　┣┓
# 　　　　　┃ 　　　　　　　┏┛
# 　　　　　┗┓┓┏━┳┓┏┛ + + + +
# 　　　　　　┃┫┫　┃┫┫
# 　　　　　　┗┻┛　┗┻┛+ + + +
"""
Author = Eric_Chan
Create_Time = 2016/03/25
introduction:
分析博文的转发趋势,获得用户之间的关系权值
"""

import re
import xlwt
import os


def walk_path(root_dir):
    """
    :param root_dir: 文件夹路径
    :return: 子文件路径以及子文件对应的上一级路径
    """
    path_tuple_list = []
    list_dirs = os.walk(root_dir)
    for root, dirs, files in list_dirs:
        print files
        if "label_link.xls" in files:  # 若存在该excel表 表示已分析过 跳过该文件夹
            continue
        for f in files:
            # if f.startswith('.'):  # 排除隐藏文件
            #     continue
            if f.startswith('uid'):
                path_tuple_list.append((root, os.path.join(root, f)))
    print path_tuple_list
    return path_tuple_list




def load_data_old(file_name):
    """
    :param file_name:
    :return:首发博文,首发博文的用户,路径用户名列表,最后发表言论博文
    """
    file1 = open(file_name)
    # line = file1.readline().decode('utf-8')
    lines = file1.readlines()
    road_list = []
    # print lines
    for line in lines[:-1]:
        if line.replace('\n', ''):
            road_list.append(line.strip().decode('utf-8'))
    # #
    # # while line:
    # #     if line.strip():
    # #         road_list.append(line.strip())
    # #         line = file1.readline().decode('utf-8')
    # #     else:
    # #         line = file1.readline().decode('utf-8')
    # print road_list, "*****"
    return road_list


def write_data_old(file_name, label_list, link_list):
    """
    将 节点对应的用户名列表 和 节点-节点-权值列表 分别写入一个 xls 的 2个sheet
    :param file_name: xls的文件名
    :param label_list: 标签列表
    :param link_list: 节点-节点-权值列表
    """
    file_0 = xlwt.Workbook(encoding='utf-8')
    table_0 = file_0.add_sheet('label')
    table_1 = file_0.add_sheet('link')
    table_0.write(0, 0, 'node')
    table_0.write(0, 1, 'label')
    for i in range(label_list.__len__()):
        table_0.write(i+1, 0, label_list.index(label_list[i]))
        table_0.write(i+1, 1, label_list[i])
    table_1.write(0, 0, 'from')
    table_1.write(0, 1, 'to')
    table_1.write(0, 2, 'weight')
    for i in range(link_list.__len__()):
        table_1.write(i+1, 0, link_list[i][0])
        table_1.write(i+1, 1, link_list[i][1])
        table_1.write(i+1, 2, link_list[i][2])
    file_0.save(file_name)



def link_label(road_list):
    pattern_name = re.compile(u'@([^@]*?)[ |:|：]')  # 匹配转发路径中出现的用户名
    link_list = []
    label_list = []
    for road in road_list:
        # print road
        name_list = re.findall(pattern_name, road)
        # print '\n'.join(name_list)
        # print
        if name_list[0] not in label_list:
            label_list.append(name_list[0])
        if name_list[1] not in label_list:
            label_list.append(name_list[1])
        link_list.append([label_list.index(name_list[0]), label_list.index(name_list[1]), 1])
    return link_list, label_list


def create_xls(topic_time_path):
    # paths = walk_path('../documents/topic')
    paths = walk_path(topic_time_path)
    # print paths
    for path in paths:
        # print path[1],
        # try:
        blog_roads = load_data_old(path[1])
        links, labels = link_label(blog_roads)
        # except:
        #     print "这个txt的格式有问题"
        #     continue
        # for l in labels:
        #     print labels.index(l), l
        # for l in links:
        #     print l
        # print 'done'
        write_data_old(path[0]+'/label_link.xls', labels, links)
    return

# if __name__ == '__main__':
#     create_xls('../documents/topic/香格里拉对话：美国防长对中国“又打又拉”/2016-06-06 22:44:48')

