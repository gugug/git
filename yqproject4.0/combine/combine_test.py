#! -*- coding:utf-8 -*-

__author__ = 'root'
import numpy as np
import copy_file
import jieba.posseg as pseg
import Levenshtein
class TextAnalyse:
    def LevenshiteinSimilarity(self,string1,string2):
        return Levenshtein.ratio(string1,string2)

    def similay(self,string1,string2):
        similar = self.LevenshiteinSimilarity(string1,string2)
        # similar = self.comsini(string1,string2)
        return similar

#     def get_cossimi(self,x,y):
#         myx=np.array(x)
#         myy=np.array(y)
#         cos1=np.sum(myx*myy)
#         cos21=np.sqrt(sum(myx*myx))
#         cos22=np.sqrt(sum(myy*myy))
#         try:
#             result =cos1/(float(cos21*cos22))
#         except:
#             result = 0
#         return result
#
#     def comsini(self,data1,data2):
#         test_words={}
#         all_words={}
#         f1_text=data1
#         f1_seg_list =pseg.cut(f1_text)
#         for w in f1_seg_list:
#             if 'n' in w.flag or 'eng' in w.flag :
#                 test_words.setdefault(w.word,0)
#                 all_words.setdefault(w.word,0)
#                 all_words[w.word]+=1
#
#         ftest1_text = data2
#         mytest1_words = copy.deepcopy(test_words)
#         ftest1_seg_list =pseg.cut(ftest1_text)
#         for w in ftest1_seg_list:
#             if 'n' in w.flag or 'eng' in w.flag :
#                 if mytest1_words.has_key(w.word):
#                     mytest1_words[w.word]+=1
#         sampdata=[]
#         test1data=[]
#         for key in all_words.keys():
#             sampdata.append(all_words[key])
#             test1data.append(mytest1_words[key])
#         test1simi=self.get_cossimi(sampdata,test1data)
#         return test1simi
#
#     def has_same_item(self,list1,list2):
#         for i1 in list1:
#             print i1
#             if i1 in list2:
#                 return True
#         return False
# # print has_same_item(data1,data2)
# # try:
# #     print comsini(data1,data2)
# # except:
# #     print 0
#
# # data1 =['语言','开心' ,'快乐' ,'欢乐']
# # data2=['文学','方法论','小说','开心' ,'快乐']
# # print has_same_item(data1,data2)

t = TextAnalyse()
# print t.similay('陈戈', '古才良')
print t.similay('上海迪士尼一个肉包35元比日本还贵网友：人傻钱多速来', '上海迪士尼一个肉包35元网友:人傻钱多速来')