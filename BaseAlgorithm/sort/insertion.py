# -*- coding: utf-8 -*-
"""
    insertion sort class
    ~~~~~~~~~~~~~~

    A class based on inserting-sort algorithm

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""

from base import BaseSort

class Insertion(BaseSort):
    """Class based on inserting-sort algorithm
    """

    def sort(self,cmp_iter_able,reverse = False):
        """sort cmp_iter_able based on inserting-sort algorithm

        Args:
            reverse: normal order(False), inverse order(True)
        """
        length = len(cmp_iter_able)
        for index_i in range(1,length):
            index_j = index_i
            while index_j>0:
                if self.compare(cmp_iter_able[index_j],cmp_iter_able[index_j-1],reverse=reverse):
                    self.exch(cmp_iter_able,index_j,index_j-1)
                index_j-=1

if __name__ == "__main__":
    # a simple test
    import random
    rand_list = []
    for i in range(20):
        rand_list.append(random.randint(0,100))

    print("Normal order")
    insert = Insertion()
    insert.sort(rand_list)
    insert.show(rand_list)
    
    print("Inverse order")
    insert.sort(rand_list,reverse=True)
    insert.show(rand_list)