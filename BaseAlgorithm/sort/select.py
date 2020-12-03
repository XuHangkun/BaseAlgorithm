# -*- coding: utf-8 -*-
"""
    select sort class
    ~~~~~~~~~~~~~~

    A class based on select sort 

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""

from base import BaseSort

class Select(BaseSort):
    """Class based on Select sort
    """

    def sort(self,cmp_iter_able,reverse = False):
        """sort cmp_iter_able based on Select sort

        Args:
            reverse: normal order(False), inverse order(True)
        """
        length = len(cmp_iter_able)
        for index_i in range(0,length-1):
            des_index = index_i
            for index_j in range(index_i+1,length):
                if not self.compare(cmp_iter_able[des_index],cmp_iter_able[index_j],reverse=reverse):
                    des_index = index_j
            self.exch(cmp_iter_able,index_i,des_index)

if __name__ == "__main__":
    # a simple test
    import random
    rand_list = []
    for i in range(20):
        rand_list.append(random.randint(0,100))

    print("Normal order")
    select = Select()
    select.sort(rand_list)
    print(select.isSorted(rand_list))
    select.show(rand_list)
    
    print("Inverse order")
    select.sort(rand_list,reverse=True)
    print(select.isSorted(rand_list,reverse=True))
    select.show(rand_list)