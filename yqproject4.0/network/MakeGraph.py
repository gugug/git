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
Create_Time = 2016/05/06
使用igraph包中的BGLL算法对社区进行社区检测
输入用户-用户权值矩阵
输出社区检测结果和社区模块度
"""

import xlrd
import igraph


def load_data(file_name, sheet_index=None):
    """
    读取xls文件,获得矩阵.
    :param file_name: xls文件路径
    :param sheet_index: xls 打开的sheet序号
    :return: 除去表头后的二元列表
    """
    if sheet_index is None:
        sheet_index = 0
    data = xlrd.open_workbook(file_name)  # 打开xls
    table = data.sheet_by_index(sheet_index)  # 打开sheet1
    all_data = table._cell_values  # 将所有数据 以二元列表进行构造
    all_data = all_data[1:]  # 除去表头
    for i in range(all_data.__len__()):  # 将表中数据的整数转化为int类型
        for j in range(all_data[0].__len__()):

            try:
                if all_data[i][j] == int(all_data[i][j]):
                    all_data[i][j] = int(all_data[i][j])
            except ValueError:
                continue
    return all_data


class MakeGraph:

    class Node:
        """
        记录每个节点的索引号，对应标签名，中心度值， 中心度值排名， 社区检测后节点所属组别， 是否为topK节点
        """
        def __init__(self):
            self.node_index = int
            self.label = ''
            self.value = int
            self.rank = int
            self.group = int
            self.is_topK = False

    def __init__(self, node_links, node_labels_dict):
        self.users_link = node_links  # 节点权值矩阵
        self.user_num = len(node_labels_dict)  # 节点个数
        self.node_list = []  # 保存每个节点属性的列表
        for i in range(self.user_num):
            self.node_list.append(self.Node())
            self.node_list[i].node_index = i
        for k, v in node_labels_dict.items():
            self.node_list[k].label = v
        self.graph = None  # 节点图
        self.divide()

    def __create_graph(self):
        """
        使用igraph构建图
        :return: graph, weights list
        """
        g = igraph.Graph(self.user_num, directed=True)
        weights = []
        edges = []
        for line in self.users_link:
            edges += [(line[0], line[1])]
            weights.append(line[2])
        g.add_edges(edges)
        node_value = g.pagerank(weights=weights)
        for i in range(self.user_num):
            self.node_list[i].value = node_value[i]
        self.graph = g
        return g, weights

    def __calculate_rank(self):
        """
        根据每个节点的pageRank值进行排名并记录
        :return:
        """
        node_values = [node.value for node in self.node_list]  # 提取节点中心度值
        node_values.sort(reverse=True)
        for node in self.node_list:
            node.rank = node_values.index(node.value)

    def __find_topK(self):
        """
        :param node_list: 节点属性列表
        :return: topK个节点属性列表
        """
        node_list = sorted(self.node_list, key=lambda c: c.value, reverse=True)
        topK_list = [node_list[0]]
        self.node_list[node_list[0].node_index].is_topK = True
        value = node_list[0].value
        for node in node_list[1:]:
            if node.value > value * 0.3 and topK_list.__len__() < self.user_num * 0.1:
                self.node_list[node.node_index].is_topK = True
                topK_list.append(node)
                value = node.value
            else:
                break
        return topK_list

    def divide(self):
        """
        使用igraph包中BGLL算法对已构建好的图进行社区检测
        并为每个节点标明
        :return:
        """
        g, weights = self.__create_graph()
        self.__calculate_rank()
        self.__find_topK()
        try:
            divide_result = g.community_walktrap(weights=weights, steps=4).as_clustering()
        except igraph._igraph.InternalError:
            g.to_undirected()
            divide_result = g.community_multilevel(weights=weights)
        for index, community in enumerate(divide_result):
            for n in community:
                self.node_list[n].group = index
        del g


# if __name__ == '__main__':
#     labels = dict(load_data('dataSet/label_link.xls', 0))
#     links = load_data('dataSet/label_link.xls', 1)
#     MG = MakeGraph(links, labels)
#     for node in MG.node_list:
#         print node.label, node.value, node.rank, node.group
    # Weibo_User = Louvain(links)
    # print Weibo_User.divide_result
    # for com in Weibo_User.divide_result:
    #     for i in com:
    #         print labels[i],
    #     print
    # print 'modularity:', Weibo_User.modularity
    # print Weibo_User.node_value_dict






