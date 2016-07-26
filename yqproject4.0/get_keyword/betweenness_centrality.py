__author__ = 'kalin'
# coding=utf-8
import networkx as nx
from semantic_similarity_network import *
from candidate_words import *


class BetweenCentrality:
    """
    :purpose:求博文词语间的点居间度
    """

    def __init__(self):
        """
        : varible:  bc_dict   词语-点居间度字典
        """
        self.G = nx.Graph()
        self.bc_dict = {}
        self.n_word = {}

    def codes_betweeness_centarlity(self, string_data):
            """
            :param string_data:
            :return: bc_dict
            """
            candidate_words_dict, nw_word, important_words = CandidateWords().get_candidate_list(string_data)
            nw_word_words = nw_word.values()
            length = len(nw_word_words)
            for i in range(length):
                self.G.add_node(i)
            E = SemanticSimilarity().similarity_network_edges(string_data)
            self.G.add_edges_from(E)
            vd= nx.betweenness_centrality(self.G, k=None, normalized=True, weight=None, endpoints=False, seed=None )
            for i in range(length):
                self.bc_dict[nw_word_words[i]] = vd[i]
            for i in range(length):
                self.n_word[i] = nw_word_words[i]
            return self.bc_dict

