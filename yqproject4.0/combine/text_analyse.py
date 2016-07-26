# coding=utf-8
__author__ = 'Har'

import Levenshtein
import igraph


class TextAnalyse:
    def __init__(self):
        pass

    def levenshtein_similarity(self, string1, string2):
        return Levenshtein.ratio(string1, string2)

    def similay(self, string1, string2):
        similar = self.levenshtein_similarity(string1, string2)
        return similar


def load_file(file_name, charset='utf-8'):
    """
    读取文件，按列返回列表
    :param file_name: 文件路径
    :param charset: 文本内容decode的编码，默认为utf-8
    :return: 文本内容列表
    """
    f1 = open(file_name)
    line = f1.readline().decode(charset).strip()
    line_list = []
    while line:
        line_list.append(line)
        line = f1.readline().decode(charset).strip()
    return line_list


class Louvain:
    divide_result = None  # 社区划分结果
    modularity = None  # 社区模块度

    def __init__(self, users_links, user_num):
        self.user_num = user_num
        self.users_link = users_links  # 用户权值矩阵
        # self.node_value_dict = {}  # 节点的中心度值 字典
        self.divide()

    def __create_graph(self):
        """
        使用igraph构建图
        :return: graph, weights list
        """
        # user_num = max([max([i[0] for i in self.users_link]), max([i[1] for i in self.users_link])]) + 1
        user_num = self.user_num
        g = igraph.Graph(user_num)
        weights = []
        edges = []
        for line in self.users_link:
            edges += [(line[0], line[1])]
            weights.append(line[2])
        g.add_edges(edges)
        # node_value = g.authority_score(weights=weights)
        # self.node_value_dict = dict(zip(range(user_num), node_value))
        return g, weights

    def divide(self):
        """
        使用igraph包中BGLL算法对已构建好的图进行社区检测
        :return:
        """
        graph, weights = self.__create_graph()
        Louvain.divide_result = graph.community_multilevel(weights=weights)
        Louvain.modularity = Louvain.divide_result.modularity


def title_cluster(title_list, rate=0.35):
    """
    :param title_list: 话题列表
    :return: 聚合话题二维列表
    """
    # print "*****"
    # print "\n".join(title_list)
    Lou = TextAnalyse()

    title_num = len(title_list)
    sim_matrix = []
    for t_0 in range(title_num):
        for t_1 in range(title_num)[t_0 + 1:]:
            if Lou.similay(title_list[t_0], title_list[t_1]) > rate:
                sim_matrix.append([t_0, t_1, 1])
    title_bgll = Louvain(users_links=sim_matrix, user_num=title_num)
    divide_result = title_bgll.divide_result
    return list(divide_result)
    # return_list = []
    # # return list(divide_result)
    # for com in divide_result:
    #     # if len(com) < 2:
    #     #     continue
    #     com_title = []
    #     for i in com:
    #         com_title.append(title_list[i])
    #     return_list.append(com_title)
    #     # print '---------------------------------------------'
    # return return_list



if __name__ == '__main__':
    # titles = load_file('title')
    # titles = ['数据瓦囧实验室', '数据挖掘实验室', '古才良', '古才良的', '我是古才良', '梁兄一坐', '一切暗号']
    titles = ['我是古才良','#梁兄一坐#', '一切暗号', '#数据瓦囧实验室#', '数据挖掘实验室', '古才良', '古才良的' ]
    print titles
    index_result = title_cluster(titles)
    print index_result
    for com in index_result:
        print "该类的代表bid及标题", com[0]
        for bid_index in com:
            # bid = bid_list[bid_index]
            print bid_index
        # print com , 'kk'
