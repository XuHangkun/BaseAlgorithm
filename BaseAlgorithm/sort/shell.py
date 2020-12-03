# -*- coding: utf-8 -*-
"""
    shell sort class
    ~~~~~~~~~~~~~~

    A class based on shell-sort algorithm

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""

from base import BaseSort

class Shell(BaseSort):
    """Class based on shell-sort algorithm
    """

    def sort(self,cmp_iter_able,reverse = False):
        """sort cmp_iter_able based on shell-sort algorithm

        Args:
            reverse: normal order(False), inverse order(True)
        """
        length = len(cmp_iter_able)
        h=1
        while h < length/3:
            h = 3*h + 1
        
        while h >= 1 :
            for i in range(h,length):
                j = i
                while j > 0:
                    if self.compare(cmp_iter_able[j],cmp_iter_able[j-h],reverse = reverse):
                        self.exch(cmp_iter_able,j,j-h)
                    j -=h
            h = h/3

if __name__ == "__main__":
    # a simple test
    import random
    rand_list = []
    for i in range(20):
        rand_list.append(random.randint(0,100))

    print("Normal order")
    shell = Shell()
    shell.sort(rand_list)
    shell.show(rand_list)
    print(shell.isSorted(rand_list))
    
    print("Inverse order")
    shell.sort(rand_list,reverse=True)
    shell.show(rand_list)
    print(shell.isSorted(rand_list,reverse=True))