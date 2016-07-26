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
        if "label_link.xls" in files:  # 若存在该excel表 表示已分析过 跳过该文件夹
            continue
        for f in files:
            if f.startswith('.'):  # 排除隐藏文件
                continue
            path_tuple_list.append((root, os.path.join(root, f)))
    return path_tuple_list


class BlogRoad:
    """
    记录博文传播路径的详细内容
    始发博文ID
    发布时间
    博文内容
    发布者ID
    发布者名
    转发路径列表
    """

    def __init__(self):
        self.blog_id = ""
        self.publish_time = ""
        self.blog_content = ""
        self.publisher_id = ""
        self.publisher_name = ""
        self.road_list = []


def load_data(file_name):
    """
    :param file_name:
    :return:首发博文,首发博文的用户,路径用户名列表,最后发表言论博文
    """
    file1 = open(file_name)
    data_save_list = []
    line = file1.readline().decode('utf-8')
    while line:
        blog_road = BlogRoad()
        # 存储首发博文ID
        blog_road.blog_id = line.strip()
        # 存储博文发布时间
        line = file1.readline().decode('utf-8')
        blog_road.publish_time = line.strip()
        # 存储博文内容
        line = file1.readline().decode('utf-8')
        blog_road.blog_content = line.strip()
        # 存储该博文的发布者的ID
        line = file1.readline().decode('utf-8')
        blog_road.publisher_id = line.strip()
        # 存储博文的发布者的用户名
        line = file1.readline().decode('utf-8')
        blog_road.publisher_name = line.strip()
        # pass
        file1.readline()
        # 存储该博文的转发路径
        line = file1.readline().decode('utf-8')
        while line:
            if line.strip():
                blog_road.road_list.append(line.strip())
                line = file1.readline().decode('utf-8')
            else:
                line = file1.readline().decode('utf-8')
                break
        data_save_list.append(blog_road)
    return data_save_list


def write_data(file_name, label_list, link_list):
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


def link_label(blog_road_list):
    """
    转发路径中, 第一个 @用户名 转发的用户名, 第二个 @用户名 为转发上一个的用户的用户名.
    若只有一个 @用户名 表明该博文是直接转发首发博文
    :param blog_road_list: BlogRoad 列表
    :return: 用户名列表, 用户-用户-权值 三元组
    """
    label_list = []  # 存储用户名列表
    link_list = []  # 用户-用户-权值 列表
    for blog_road in blog_road_list:
        if blog_road.publisher_name not in label_list:
            label_list.append(blog_road.publisher_name)
        first_sy = label_list.index(blog_road.publisher_name)  # 发布者用户名的ID
        pattern_name = re.compile(u'@(.*?)?[：:]')  # 匹配转发路径中出现的用户名
        for road in blog_road.road_list:
            name_list = re.findall(pattern_name, road)
            if name_list.__len__() > 1:
                if name_list[0] not in label_list:
                    label_list.append(name_list[0])
                if name_list[1] not in label_list:
                    label_list.append(name_list[1])
                link_list.append([label_list.index(name_list[0]), label_list.index(name_list[1]), 1])
            else:
                if name_list[0] not in label_list:
                    label_list.append(name_list[0])
                link_list.append([label_list.index(name_list[0]), first_sy, 1])
    return link_list, label_list


if __name__ == '__main__':
    paths = walk_path('topic')
    for path in paths:
        blog_roads = load_data(path[1])
        links, labels = link_label(blog_roads)
        # for l in labels:
        #     print labels.index(l), l
        # for l in links:
        #     print l
        print path[1], 'done'
        write_data(path[0]+'/label_link.xls', labels, links)
