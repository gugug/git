# coding=utf-8
from MakeGraph import *
from DrawGraph import *
from links_labels import *
import xlwt
import os

def write_data(file_name, node_list, link_list):
    """
    将节点的信息重新保存一份带value的
    :param link_list:
    :param file_name: 保存路径
    :param node_list:
    :return:
    """
    file_0 = xlwt.Workbook(encoding='utf-8')
    table_0 = file_0.add_sheet('label')
    table_1 = file_0.add_sheet('link')
    table_0.write(0, 0, 'node')
    table_0.write(0, 1, 'label')
    table_0.write(0, 2, 'value')
    for i in range(node_list.__len__()):
        table_0.write(i + 1, 0, i)
        table_0.write(i + 1, 1, node_list[i].label)
        if node_list[i].is_topK:
            table_0.write(i + 1, 2, 5)
        else:
            table_0.write(i + 1, 2, 1)
    table_1.write(0, 0, 'from')
    table_1.write(0, 1, 'to')
    table_1.write(0, 2, 'weight')
    for i in range(link_list.__len__()):
        table_1.write(i + 1, 0, link_list[i][0])
        table_1.write(i + 1, 1, link_list[i][1])
        table_1.write(i + 1, 2, link_list[i][2])
    file_0.save(file_name)


def main_network(topic_time_path):
    # labels = dict(load_data('dataSet/label_link.xls', 0))  # 标签列表
    # links = load_data('dataSet/label_link.xls', 1)  # 节点连接列表
    # MG = MakeGraph(links, labels)
    # DrawGraph(node_list=MG.node_list, graph=MG.graph).draw_graph('result/SNA.png')
    # write_data('result/new_label_link.xls', MG.node_list, links)
    # print "节点索引 节点标签名 节点pageRank值 节点排名 是否为topK节点"
    # for node in MG.node_list:
    #     print node.node_index, node.label, node.value, node.rank, node.group, node.is_topK


    path_list = []
    dir_list = []
    pic_dir_list = []
    create_xls(topic_time_path)
    for root, dir, file in os.walk(topic_time_path):
        if "label_link.xls" in file:
            dir_list.append(root)
            pic_dir = root.replace('documents','static/sna')
            pic_dir_list.append(pic_dir)
            path = os.path.join(root,'label_link.xls')
            path_list.append(path)
    # print path_list[0]
    for i in range(len(path_list)):
        # print 'pc',pic_dir_list[i]
        #     print path_list[i],'op'
            labels = dict(load_data(path_list[i], 0))  # 标签列表
            links = load_data(path_list[i], 1)  # 节点连接列表
            if links.__len__() == 0:
                print "分析的路径为空,跳过"
                continue
            # print path_list[i]

            MG = MakeGraph(links, labels)
            DrawGraph(node_list=MG.node_list, graph=MG.graph).draw_graph(os.path.join(pic_dir_list[i], 'SNA.png'))
            write_data(os.path.join(dir_list[i], 'new_label_link.xls'), MG.node_list, links)
            print "done done done"
            # print "节点索引 节点标签名 节点pageRank值 节点排名 是否为topK节点"
            # for node in MG.node_list:
            #     print node.node_index, node.label, node.value, node.rank, node.group, node.is_topK


# main_network('../documents/topic/香格里拉对话：美国防长对中国“又打又拉”/2016-06-06 22:44:48')