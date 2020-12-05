# -*- coding: utf-8 -*-
"""
    base
    ~~~~~~~~~~~~~~

    make a base sort class

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""

class BaseSort:
    """base class for sort
    """

    def __init__(self):
        pass

    def sort(self,cmp_iter_able,reverse = False):
        pass

    def smaller(self,cmp_i,cmp_j):
        """compare cmp_i and cmp_j

        Returns:
            True : cmp_i is smaller than (or equal to) cmp_j
            False: cmp_i is bigger than  cmp_j
        """
        return cmp_i <= cmp_j
    
    def bigger(self,cmp_i,cmp_j):
        """compare cmp_i and cmp_j

        Returns:
            True : cmp_i is bigger than (or equal to) cmp_j
            False: cmp_i is smaller than  cmp_j
        """
        return cmp_i >= cmp_j

    def compare(self,cmp_i,cmp_j,reverse=False):
        """compare cmp_i and cmp_j

        Args:
            reverse : use smaller(False) or bigger(True) 
        """
        if reverse:
            return self.bigger(cmp_i,cmp_j)
        else:
            return self.smaller(cmp_i,cmp_j)    
    
    def exch(self,cmp_iter_able,i,j):
        """exchange i'th item and j'th item in cmp_iter_able
        """
        tmp = cmp_iter_able[i]
        cmp_iter_able[i] = cmp_iter_able[j]
        cmp_iter_able[j] = tmp

    def show(self,cmp_iter_able):
        """print cmp_iter_able
        """
        try:
            length = len(cmp_iter_able)
        except (TypeError,AttributeError):
            print("cmp_iter_able has no len()")
            raise
        except:
            print("Unexcept error")
            raise
            
        for i in range(0,length):
            print(cmp_iter_able[i])
        
    
    def isSorted(self,cmp_iter_able,reverse = False):
        """judge id cmp_iter_able is sorted

        Args:
            reverse : normal ordering(False) or reverse ordering(True)
        
        returns:
            True : being sorted
            False: not being sorted
        """
        try:
            length = len(cmp_iter_able)
        except (TypeError,AttributeError):
            print("cmp_iter_able has no len()")
            raise
        except:
            print("Unexcept error")
            raise
            
        for i in range(0,length-1):
            if not self.compare(cmp_iter_able[i],cmp_iter_able[i+1],reverse=reverse):
                return False
        return True

if __name__ == "__main__":
    #this is a simple test example. [test pass]
    test_sort = BaseSort()
    print("test smaller")
    print("1 < 2 :",test_sort.compare(1,2))
    print("1 <= 1 :",test_sort.compare(1,1))
    print("2 < 1 :",test_sort.compare(2,1))

    print("test bigger")
    print("2 > 1 :",test_sort.compare(2,1,reverse=True))
    print("1 <= 1 :",test_sort.compare(1,1,reverse=True))
    print("1 > 2 :",test_sort.compare(1,2,reverse=True))

    print("test isSorted")
    print("range(0,10) normal order ? ",test_sort.isSorted(range(0,10)))
    print("range(0,10) reverse order ? ", test_sort.isSorted(range(0,10),reverse=True))
    print("range(10,0,-1) normal order ? ", test_sort.isSorted(range(10,0,-1)))
    print("range(10,0,-1) reverse order ? ", test_sort.isSorted(range(10,0,-1),reverse=True))