# -*- coding: utf-8 -*-
"""
    merge sort class
    ~~~~~~~~~~~~~~

    A class based on merge-sort algorithm (top-down)

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""

from BaseAlgorithm.sort.base import BaseSort

class Merge(BaseSort):
    """Class based on merge sort (top-down)
    """

    def __init__(self):
        self.__aux = []

    def __merge(self,cmp_iter_able,lo:int,mid:int,hi:int,reverse):
        """merge cmp_iter_able[lo..mid] and merge cmp_iter_able[mid..hi]
        """
        i = lo
        j = mid + 1
        for k in range(lo,hi + 1):
            self.__aux[k] = cmp_iter_able[k]
        
        for k in range(lo,hi + 1):
            if i > mid :
                cmp_iter_able[k] = self.__aux[j]
                j += 1
            elif j > hi :
                cmp_iter_able[k] = self.__aux [i]
                i += 1
            elif self.compare(self.__aux[j],self.__aux[i],reverse=reverse):
                cmp_iter_able[k] = self.__aux[j]
                j += 1 
            else:
                cmp_iter_able[k] = self.__aux[i]
                i += 1
    
    def sort(self,cmp_iter_able,reverse = False):
        """sort cmp_iter_able based on merge sort

        Args:
            reverse: normal order(False), inverse order(True)
        """
        length = len(cmp_iter_able)
        self.__aux = [0 for i in range(length)]
        self.__sort_iter(cmp_iter_able,0,length-1,reverse)
        
    
    def __sort_iter(self,cmp_iter_able,lo:int,hi:int,reverse):
        """ sort function used to do iteration
        """
        if hi <= lo :
            return
        mid = lo + int(( hi - lo )/2)
        self.__sort_iter(cmp_iter_able,lo,mid,reverse)
        self.__sort_iter(cmp_iter_able,mid+1,hi,reverse)
        self.__merge(cmp_iter_able,lo,mid,hi,reverse)

if __name__ == "__main__":
    # a simple test
    import random
    rand_list = []
    for i in range(20):
        rand_list.append(random.randint(0,100)*0.9)

    print("Normal order")
    merge = Merge()
    merge.sort(rand_list)
    merge.show(rand_list)
    print(merge.isSorted(rand_list))
    
    print("Inverse order")
    merge.sort(rand_list,reverse=True)
    merge.show(rand_list)
    print(merge.isSorted(rand_list,reverse=True))