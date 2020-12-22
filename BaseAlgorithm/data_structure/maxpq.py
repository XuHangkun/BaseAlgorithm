# -*- coding: utf-8 -*-
"""
    Max priority queue
    ~~~~~~~~~~~~~~

    a max priority class. (Alought python has it's built-in list, 
    we will achieve this data structure by ourself. We will only
    use some basic functions of python so we can display the 
    details of list.)

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""

class MaxPQ:
    """max priority class
    """

    def __init__(self,eg_type):
        """eg_type: you need to input a item type (for eg. 3.5)
                    to illustrate which queue you want to create
        """
        self.__pq=[eg_type]
        self.__Num=0

    def isEmpty(self):
        return self.__Num == 0

    def size(self):
        return self.__Num

    def smaller(self,cmp_i,cmp_j):
        return self.__pq[cmp_i] <  self.__pq[cmp_j]
    
    def __exch(self,i:int,j:int):
        """exchange i'th item and j'th item
        """
        key = self.__pq[i]
        self.__pq[i] = self.__pq[j]
        self.__pq[j] = key
    
    def __swim(self,k:int):
        """order the queue from bottom to top
        """
        while k>1 and self.smaller(int(k/2),k):
            self.__exch(int(k/2),k)
            k = int(k/2)
    
    def __sink(self,k:int):
        """order the queue from top to bottom
        """
        while 2 * k <= self.__Num :
            j = 2 * k
            if j < self.__Num and self.smaller(j,j+1):
                j = j + 1
            if not self.smaller(k,j):
                break
            self.__exch(k,j)
            k = j
    
    def insert(self,item):
        """insert a item
        """
        self.__Num = self.__Num + 1
        self.__pq.append(item)
        self.__swim(self.__Num)
    
    def delMax(self):
        """delete the maxium item in the queue and return the item
        """
        if self.isEmpty():
            return None
        
        item = self.__pq[1]
        self.__exch(1,self.__Num)
        del self.__pq[self.__Num]
        self.__Num = self.__Num - 1
        self.__sink(1)
        return item
    
    def show(self):
        """show the queue
        """
        for i in range(1,self.__Num + 1):
            print(self.__pq[i])

if __name__ == "__main__":
    import random
    eg_pq = MaxPQ(3)
    for i in range(15):
        eg_pq.insert(random.randint(0,20))
    #eg_pq.show()
    print(eg_pq.delMax())
    eg_pq.show()