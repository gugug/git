__author__ = 'kalin'
# coding=utf-8
from betweenness_centrality import  *
from collections import Counter
from candidate_words import *
import os
import time



class Keyword():
    """
    :purpose :获得关键词
    """

    def __init__(self):
        """
        :varible poss:词性-词性权重字典
        :varible word_length: 词-词长字典
        """
        self.poss = {}
        self.word_length={}
        self.word_score = {}
        self.import_w = []

    def feature(self, string_data):
        """
        :purpose :获得词语的统计特征值(词性,词频,词长)
        :param string_data:
        :return: (pos, words_tf_dict, self.word_length, nw_word_words)
        """
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, 'tag.txt')
        files = open(file_path, "r")
        file = files.readlines()
        for line in file:
            s = line.strip().split(' ')
            self.poss[s[0]] = s[1]
        po = self.poss
        candidate_words_dict, n_word, important_words = CandidateWords().get_candidate_list(string_data)
        nw_word_words = n_word.values()   #order words
        pos = {}   #词-词性权重字典
        for word in nw_word_words:
            if word in important_words:
                self.import_w.append(word)
            self.word_length[word] = len(word)/3
            if candidate_words_dict[word] in po.keys():
                pos[word] = float(po[candidate_words_dict[word]])
            else:
                pos[word] = 0.1
        words_tf_dict = dict(Counter(nw_word_words))
        files.close()
        return pos, words_tf_dict, self.word_length, nw_word_words,self.import_w

    def score(self, string_data):
        """
        :purpose : 计算词语关键度,并排序
        :param string_data:
        :return rank : 词语关键度
        """
        tw = 0.4     #统计特征权重
        vdw = 0.6    #居间度权重
        lenw = 0.1   #词长权重
        posw = 0.8
        tfw = 0.6  #词频权重
        pos, words_tf_dict, word_length, candidate_word,import_w = self.feature(string_data)
        vd = BetweenCentrality().codes_betweeness_centarlity(string_data)
        for word in candidate_word:
            if word in import_w:
                 s = (vd[word] * vdw)+0.8+(tw * (word_length[word] * lenw + pos[word] * posw + words_tf_dict[word]*tfw))
            else:
                s = (vd[word] * vdw) + (tw * (word_length[word] * lenw + pos[word] * posw + words_tf_dict[word]*tfw))
            self.word_score[word] = s
        rank = sorted(self.word_score.iteritems(), key=lambda d: d[1], reverse=True)
        return rank

    def keyword(self, string_data):
            """
            :param string_data:
            :return keywords: 关键词
            """
            start = time.clock()
            key_score = self.score(string_data)
            keywords = []
            # 输出前几个关键词
            for key in key_score[0:4]:
                # print key[0]
                keywords.append(key[0])
            end = time.clock()
            # print "read  score(): %f  s" % (end-start)
            return keywords

    def combine_keywords(self, string_data):
        """
        提取关键字
        :param string_data: 输入文本，需要被提取的文本（string）
        :return: 提取的关键字（string）
        """
        a = self.keyword(string_data)
        combine_keywords = ''
        for i in a:
            combine_keywords += (i + ' ')
        return combine_keywords


# if __name__ == "__main__":
#     a = Keyword().combine_keywords('【年轻人广场玩“彩虹跑” 满地粉末愁坏清洁工】近日，一群青年在成都萃锦西路的公共广场开展“彩虹跑”活动，留下一片狼藉，地面遍布彩色粉末，风一吹便扬起粉尘。如何清理难坏清洁工。主办方称粉末是染色玉米粉，有人清理，但直到清洁工清理完毕，也未见商家工作人员来清扫。年轻人广场上玩“彩虹跑” 满地粉末愁怀清洁工 [组图共2张]')
#     print a

