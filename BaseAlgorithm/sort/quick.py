# -*- coding: utf-8 -*-
"""
    quick sort class
    ~~~~~~~~~~~~~~

    A class based on quick sort 

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""

from BaseAlgorithm.sort.base import BaseSort
import random

class Quick(BaseSort):
    """Class based on quick-sort algorithm
    """

    def sort(self,compare_iter_able,reverse = False):
        """shuffle is important here
        """
        random.shuffle(compare_iter_able)
        self.__sort_iter(compare_iter_able,0,len(compare_iter_able)-1,reverse = reverse)
    
    def __sort_iter(self,compare_iter_able,lo:int,hi:int,reverse):
        """sort function used to do iteration
        """
        if hi <= lo :
            return

        j = self.__partition(compare_iter_able,lo,hi,reverse = reverse)
        self.__sort_iter(compare_iter_able,lo,j-1,reverse = reverse)
        self.__sort_iter(compare_iter_able,j+1,hi,reverse=reverse)

    def __partition(self,compare_iter_able,lo:int,hi:int,reverse):
        i = lo
        j = hi
        cmp = compare_iter_able[lo]
        while True:
            while self.compare(compare_iter_able[i],cmp,reverse=reverse):
                if i + 1 > hi :
                    break
                i = i + 1
            while self.compare(cmp,compare_iter_able[j],reverse=reverse):
                if j - 1 < lo:
                    break
                j = j - 1
            if i >= j  :
                break
            self.exch(compare_iter_able,i,j)
        self.exch(compare_iter_able,lo,j)
        return j


if __name__ == "__main__" :
    # a simple test
    import random
    rand_list = []
    quick = Quick()
    for i in range(20):
        rand_list.append(random.randint(0,100)*0.9)
    quick.sort(rand_list)
    quick.show(rand_list)
    print(quick.isSorted(rand_list))

    #quick sort need more test
    for i in range(30):
        rand_list = []
        for j in range(300):
            rand_list.append(random.randint(0,100)*0.9)
        quick.sort(rand_list,reverse=True)
        print(quick.isSorted(rand_list,reverse=True))