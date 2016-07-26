__author__ = 'kalin'
# coding=utf-8
from candidate_words import *
import numpy
import os


class SemanticSimilarity():
    """
    :purpose: 获得博文词语之间的语义相似网络的边集
    """
    def __init__(self):
        """
        :varible word_tag_dict : 词-语义编号词典
        :varible E: 边集
        """
        self.word_tag_dict = {}
        self.E = []

    def word_tag_dictionary(self):
            """
            :return: word_tag_dict
            """
            #获取当前文件夹的绝对路径
            base_dir = os.path.dirname(__file__)
            #获取当前文件夹内的文件
            file_path = os.path.join(base_dir, 'word_codes.txt')
            files = open(file_path, "r")
            table = files.readlines()
            for code in table:
                    code = code.strip()
                    codes = code.split(' ')
                    self.word_tag_dict[codes[0]] = codes[1:]
            files.close()
            return self.word_tag_dict

    def similarity(self, i, j, nwword_words, word_tag_dict):
            """
            :varible  weights_set : 语义差异的权重列表
            :varible  list : 列表中放的是两个词的多组编号之间语义的差异大小
            :purpose : 求两个词之间的语义相似度
            :param i: 词1位置
            :param j: 词2位置
            :param candidate_word:
            :param word_tag_dict:
            :return sim :  语义相似度
            """
            weights_set = [1.0,0.5,0.25,0.25,0.125,0.06,0.06,0.03]
            alpha = 5
            init_dis = 10
            list = []
            w1 = nwword_words[i]
            w2 = nwword_words[j]
            code1 = word_tag_dict[w1]
            code2 = word_tag_dict[w2]
            #比较语义编码
            for m in range(len(code1)):
                for n in range(len(code2)):
                    diff = -1
                    for k in range(len(code2[n])):
                        if code1[m][k] != code2[n][k]:    # compare code
                            diff = k
                            list.append(diff)
                            break
                    if (diff == -1) and (code2[n][7] != u'#'):
                            sim = 1.0
                            return sim
                    elif (diff == -1) and (code2[n][7] == u'#'):
                            min_dis = weights_set[7]*init_dis
                            sim = alpha / (min_dis+alpha)
                            return sim
            diff = min(list)
            min_dis = weights_set[diff]*init_dis
            sim = alpha / (min_dis+alpha)
            return sim

    def similar_matrixs(self, string_data):
            """
            :purpose :填充相似度矩阵
            :param string_data:
            :return  similar_matrix: 相似度矩阵
            """
            word_tag_dict = self.word_tag_dictionary()
            keys = word_tag_dict.keys()
            candidate_words_dict, nwword, important_words = CandidateWords().get_candidate_list(string_data)
            nwword_words = nwword.values()   #order words
            length = len(nwword_words)
            similar_matrix = numpy.zeros(shape=(length,length))
            #列表里放的是同时在博文和同义词词林中出现的词
            word_list =[]
            for word in nwword_words:
                if word in keys:
                    word_list.append(word)
            for i in range(length):
                for j in range(length):
                    if (nwword_words[i] in word_list) and (nwword_words[j] in word_list):
                        similar_matrix[i][j] = self.similarity(i, j, nwword_words, word_tag_dict)
                    else:
                        similar_matrix[i][j] = 0.33
            return similar_matrix

    def similarity_network_edges(self, string_data):
            """
            :purpose : 为语义相似网络图填边
            :param string_data:
            :return E
            """
            similar_matrix = self.similar_matrixs(string_data)
            row_col = similar_matrix.shape
            for i in range(row_col[0]):
                for j in xrange(i+1, row_col[0]):
                    # 两词语义相似度大于一点阈值,为这两词建立边的关系
                    if similar_matrix[i][j] > 0.4:
                        self.E.append((i, j))
            return self.E


