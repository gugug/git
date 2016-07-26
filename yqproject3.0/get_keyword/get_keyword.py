__author__ = 'kalin'
# coding=utf-8
from betweenness_centrality import  *
from collections import Counter
from candidate_words import *
import os
import time

class Keyword():

    def __init__(self):
        self.poss = {}   #词性表
        self.word_length={}
        self.word_score = {}

    def feature(self, string_data):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, 'tag.txt')
        files = open(file_path, "r")
        file = files.readlines()
        for line in file:
            s = line.strip().split(' ')
            self.poss[s[0]] = s[1]
        po = self.poss
        candidate_words_dict, nword = CandidateWords().get_candidate_list(string_data)
        nwword_words = nword.values()   #order words
        pos = {}
        for word in nwword_words:
            self.word_length[word] = len(word)/3
            if candidate_words_dict[word] in po.keys():
                pos[word] = float(po[candidate_words_dict[word]])
            else:
                pos[word] = 0.1
        words_tf_dict = dict(Counter(nwword_words))
        files.close()
        return (pos, words_tf_dict, self.word_length, nwword_words)

    def score(self, string_data):
        tw = 0.4
        vdw = 0.6
        lenw = 0.1
        posw = 0.5
        tfw = 0.8
        pos, words_tf_dict, word_length, candidate_word = self.feature(string_data)
        vd = BetweenCentrality().codes_betweeness_centarlity(string_data)
        for word in candidate_word:
            s = (vd[word] * vdw) + (tw * (word_length[word] * lenw + pos[word] * posw + words_tf_dict[word]*tfw))
            self.word_score[word] = s
        rank = sorted(self.word_score.iteritems(), key=lambda d: d[1], reverse=True)
        return rank

    def keyword(self, string_data):
        start = time.clock()
        key_score = self.score(string_data)
        keywords = []
        for key in key_score[0:3]:
            keywords.append(key[0])
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
#      a = Keyword().combine_keywords('【年轻人广场玩“彩虹跑” 满地粉末愁坏清洁工】近日，一群青年在成都萃锦西路的公共广场开展“彩虹跑”活动，留下一片狼藉，地面遍布彩色粉末，风一吹便扬起粉尘。如何清理难坏清洁工。主办方称粉末是染色玉米粉，有人清理，但直到清洁工清理完毕，也未见商家工作人员来清扫。年轻人广场上玩“彩虹跑” 满地粉末愁怀清洁工 [组图共2张]')
#      print a

