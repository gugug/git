__author__ = 'kalin'
# coding=utf-8
from candidate_words import *
import numpy
import os


class Semantic_similarity():
    def __init__(self):
        self.word_tag_dict = {}
        self.E = []

    def word_tag_dictionary(self):
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

    def similarity(self, i, j, candidate_word, word_tag_dict):
            weights_set = [1.0,0.5,0.25,0.25,0.125,0.06,0.06,0.03]
            alpha = 5
            init_dis = 10
            list=[]
            w1 = candidate_word[i]
            w2 = candidate_word[j]
            code1 = word_tag_dict[w1]
            code2 = word_tag_dict[w2]
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
            word_tag_dict = self.word_tag_dictionary()
            keys = word_tag_dict.keys()
            candidate_words_dict, nwword = CandidateWords().get_candidate_list(string_data)
            nwword_words = nwword.values()   #order words
            length = len(nwword_words)
            similar_matrix = numpy.zeros(shape=(length,length))
            word_list =[]
            for word in nwword_words:
                if word in keys:
                    word_list.append(word)
            for i in range(length):
                for j in range(length):
                    if (nwword_words[i] in word_list) and (nwword_words[j] in word_list):
                        similar_matrix[i][j] = self.similarity(i, j, nwword_words, word_tag_dict)
                    else:
                        similar_matrix[i][j] = 0.85
            return similar_matrix

    def similarity_network_edges(self, string_data):
        similar_matrix = self.similar_matrixs(string_data)
        row_col = similar_matrix.shape
        for i in range(row_col[0]):
            for j in xrange(i+1, row_col[0]):
                if similar_matrix[i][j] > 0.66:
                    self.E.append((i, j))
        return self.E

