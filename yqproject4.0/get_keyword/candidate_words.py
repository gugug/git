__author__ = 'kalin'
# coding=utf-8
import jieba
import jieba.posseg as pseg      #words tagging
import os
import re

class CandidateWords:
        """
        :purpose:对博文进行处理,得到词-词性字典,序号-词字典,待以后续利用
        """

        def __init__(self):
            """
            :varible  stop_ws :  停用词列表
            :varible  candidate_word  : 按句子顺序以及经过取停用词后的词列表
            :varible  lag : 词性列表
            :varible  candidate_dict  : 词-词性字典,键为单词,值为词性
            :varible  n_word :  序号-词字典,键为词的序号,值为词
            :varible  important_words : 【】里的词, 列表
            :varible  emo_sign : 表情
            """
            self. stop_ws = []
            self.candidate_word = []
            self.flag = []
            self.candidate_dict = {}
            self.n_word = {}
            self.important_words = []
            self.emo_sign = []

        def stop_wd(self):
            """
            :return: stop_ws
            """
            base_dir = os.path.dirname(__file__) #获取当前文件夹的绝对路径
            file_path = os.path.join(base_dir, 'stopwords.txt')  #获取当前文件夹内的文件
            files = open(file_path, "r") #读取文件
            stopword = files.readlines()
            for line in stopword:
                sw = line.strip('\n')
                sw = sw.decode('utf-8')# type is str
                self.stop_ws.append(sw)
            files.close()
            return self.stop_ws

        def get_candidate_list(self, string_data):
                """
                :param string_data:
                :return: (candidate_dict, n_word)
                """
                stop = self.stop_wd()
                match = re.findall(pattern=re.compile('【.*?】'), string =string_data)
                f_match = list(jieba.cut("".join(match)))
                emotion = re.findall(pattern=re.compile('\[(.*?)\]'), string="".join(match))
                for e in emotion:
                    s = e.decode("utf-8")
                    self.emo_sign.append(s)
                # 去除表情
                for s in self.emo_sign:
                    if s in f_match:
                        f_match.remove(s)
                importance = jieba.cut("".join(f_match))
                import_word = list(importance)
                for i in import_word:
                    if i not in stop:
                        self.important_words.append(i.encode("utf-8"))
                words_tags = list(pseg.cut(string_data))
                word_tag =[]
                words_tag=[]
                for w in words_tags:
                    word_tag.append(w.word)
                for w in word_tag:
                    words_tag.append(w)
                    if w =='[':
                        word_tag.remove( word_tag[word_tag.index(w)+1])
                string = "".join(words_tag)
                words_tags = pseg.cut(string)
                for w in words_tags:
                    if w.flag != u'x' and (w.word not in stop) and len(w.word) != 1:
                        self.candidate_word.append(w.word.encode("utf-8"))
                        self.flag.append(w.flag.encode("utf-8"))
                for i in range(len(self.flag)):
                        self.candidate_dict[self.candidate_word[i]] = self.flag[i]   #disorder dict (word:flag)
                for i in range(len(self.candidate_word)):
                        self.n_word[i] = self.candidate_word[i]
                return self.candidate_dict,  self.n_word,self.important_words


