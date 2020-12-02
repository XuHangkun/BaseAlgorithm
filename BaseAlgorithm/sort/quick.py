# -*- coding: utf-8 -*-
"""
    quick sort class
    ~~~~~~~~~~~~~~

    A class based on quick sort 

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""
from base import BaseSort

class Quick(BaseSort):
    """Class based on quick sort
    """

    def sort(self,cmp_iter_able,reverse = False):
        """sort cmp_iter_able based on quick sort

        Args:
            reverse: normal order(False), inverse order(True)
        """
        length = len(cmp_iter_able)
        for index_i in range(0,length-1):
            des_index = index_i
            for index_j in range(index_i+1,length):
                if not self.compare(cmp_iter_able[index_i],cmp_iter_able[index_j],reverse=reverse):
                    des_index = index_j
            self.exch(cmp_iter_able,index_i,des_index)

if __name__ == "__main__":
    # a simple test
    import random
    rand_list = []
    for i in range(20):
        rand_list.append(random.randint(0,100))

    print("Normal order")
    quick = Quick()
    quick.sort(rand_list)
    quick.show(rand_list)
    
    print("Inverse order")
    quick.sort(rand_list,reverse=True)
    quick.show(rand_list)