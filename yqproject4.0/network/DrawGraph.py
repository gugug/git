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
Create_Time = 2016/05/07
使用igraph包 划分社区图
输入igraph.Graph(), node_list
输出 社区划分图
"""
import igraph

color_dict = {0: "pink", 1: "green", 2: "purple", 3: "orange", 4: "blue", 5: "yellow", 6: "red", 7: "#8B2500",
              8: "#87CEEB", 9: "#707070",
              10: "#FFF68F", 11: "#FFEFD5", 12: "#FFE4E1", 13: "#FFDEAD", 14: "#FFC1C1", 15: "#FFB90F", 16: "#FFA54F",
              17: "#FF8C00",
              18: "#698B69", 19: "#FF6EB4", 20: "#FF4500", 21: "#FF3030", 22: "#F5DEB3", 23: "#F0FFFF", 24: "#F08080",
              25: "#EED2EE", 26: "#EECFA1",
              27: "#EECBAD", 28: "#EEC900", 29: "#DDA0DD", 30: "#E3E3E3", 31: "#DB7093", 32: "#D8BFD8", 33: "#D2B48C",
              34: "#CDCDB4",
              35: "#CDAD00", 36: "#CD853F", 37: "#CD5555", 38: "#CAE1FF", 39: "#BCEE68", 40: "#A0522D", 41: "#AEEEEE",
              42: "#9AFF9A",
              43: "#B03060", 44: "#8B6508", 45: "#8B475D", 46: "#8B1A1A", 47: "#836FFF", 48: "#7A378B", 49: "#76EEC6",
              50: "black"
              }


class DrawGraph:

    def __init__(self, graph, node_list):
        """
        :param graph: igraph.Graph()
        :param node_list: [.label .value .rank .group, ]
        """
        self.graph = graph
        self.node_list = node_list

    def draw_graph(self, file_name):
        """
        :param file_name:
        :return:
        """
        graph = self.graph
        node_list = self.node_list
        layout = graph.layout_fruchterman_reingold()
        v_size_list = []  # 记录节点大小的列表
        v_color_list = []  # 记录节点颜色的列表
        v_label_list = []  # 记录标签名的列表
        for node in node_list:
            v_size_list.append(300*node.value+10)
            v_color_list.append(color_dict[node.group])
            v_label_list.append(node.label.encode('utf-8'))

        p = igraph.Plot()
        p.background = "#f0f0f0"  # 将背景改为白色，默认是灰色网格

        p.add(graph,
              bbox=(50, 50, 550, 550),  # 设置图占窗体的大小，默认是(0,0,600,600)
              layout=layout,  # 图的布局
              vertex_size=v_size_list,  # 点的尺寸
              edge_width=0.5, edge_color="grey",  # 边的宽度和颜色，建议灰色，比较好看
              vertex_label_size=8,  # 点标签的大小
              vertex_label=v_label_list,
              vertex_color=v_color_list,)  # 为每个点着色
        p.save(file_name)  # 将图保存到特定路径，igraph只支持png和pdf
        p.remove(graph)  # 清除图像

