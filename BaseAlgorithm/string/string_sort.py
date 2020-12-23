# -*- coding: utf-8 -*-
"""
    sort algrithms of string
    ~~~~~~~~~~~~~~

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""
from BaseAlgorithm.sort.insertion import Insertion

class LSD:
    """Low priority string sort
    """
    def __init__(self,R=256):
        self.R = R


    def sort(self,string_list,w:int):
        """sort strings in list according to w chars
        """
        strs_len = len(string_list)
        R = self.R
        aux = []
        for index in range(strs_len):
            aux.append("")
        for d in range(w-1,-1,-1):
            count = []
            for i in range(R + 1):
                count.append(0)
            for i in range(strs_len):
                count[ord(string_list[i][d]) + 1] += 1
            for r in range(R):
                count[r+1] += count[r]
            for i in range(strs_len):
                aux[count[ord(string_list[i][d])]] = string_list[i]
                count[ord(string_list[i][d])] += 1
            for i in range(strs_len):
                string_list[i] = aux[i]
    
    
class MSD:
    """high priority string sort
    """
    
    def __init__(self,R=256,M=15):
        self.R = R
        self.M = M
        self.aux = []

    def charAt(self,str,d):
        if d<len(str):
            return ord(str[d])
        else:
            return -1
    
    def sort(self,str_list):
        N = len(str_list)
        for i in range(N):
            self.aux.append("")
        self.__sort(str_list,0,N-1,0)

    def __sort(self,str_list,lo,hi,d):
        if hi <= lo + self.M:
            self.insertion(str_list,lo,hi)
            return
        count = []
        for i in range(self.R + 2):
            count.append(0)
        for i in range(lo,hi + 1):
            count[self.charAt(str_list[i],d) + 2] += 1
        for r in range(self.R+1):
            count[r+1] += count[r]
        for i in range(lo,hi+1):
            self.aux[count[self.charAt(str_list[i],d) + 1]] = str_list[i]
            count[self.charAt(str_list[i],d) + 1] += 1
        for i in range(lo,hi +1):
            str_list[i] = self.aux[i - lo]
        for r in range(self.R):
            self.__sort(str_list,lo + count[r],lo + count[r + 1] - 1,d + 1)
    
    def insertion(self,cmp_iter_able,lo,hi):
        """sort cmp_iter_able based on inserting-sort algorithm
        """

        for index_i in range(lo,hi + 1):
            index_j = index_i
            while index_j>lo:
                if cmp_iter_able[index_j] < cmp_iter_able[index_j-1]:
                    tmp = cmp_iter_able[index_j]
                    cmp_iter_able[index_j] = cmp_iter_able[index_j-1]
                    cmp_iter_able[index_j-1] = tmp
                index_j-=1
