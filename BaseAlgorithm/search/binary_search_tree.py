# -*- coding: utf-8 -*-
"""
    binary search tree
    ~~~~~~~~~~~~~~

    make a binary search tree class

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""

class BSTNode:
    """node of binary search tree
    """
    def __init__(self,key=None,value=None,N=0,left=None,right=None):
        #key should be comparable
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.N = N

class BST:
    """binary search tree class

       use binary search class
    """

    def __init__(self):
        #point to root  node
        self.root = None
    
    def size(self):
        """get size of BST
        """
        return self.__size(self.root)

    def __size(self,node):
        if not node:
            return 0
        else:
            return node.N

    def get(self,key):
        """get value of the key
        """
        return self.__get(self.root,key)
    
    def __get(self,node,key):
        if not node:
            return None
        if node.key < key:
            return self.__get(node.right,key)
        elif node.key > key:
            return self.__get(node.left,key)
        else:
            return node.value    
        
    def put(self,key,value):
        """put a node into the tree
        """
        self.root = self.__put(self.root,key,value)
    
    def __put(self,node,key,value):
        if not node:
            return BSTNode(key,value,1)
        if key < node.key:
            node.left = self.__put(node.left,key,value)
        elif key > node.key:
            node.right = self.__put(node.right,key,value)
        else:
            node.value = value
        node.N = self.__size(node.left) + self.__size(node.right) + 1
        return node
    
    def show(self):
        """print the tree in order
        """
        self.__show(self.root)
    
    def __show(self,node):
        if not node:
            return
        if node.left:
            self.__show(node.left)
        print((node.key,node.value))
        if node.right:
            self.__show(node.right)
    
    def min(self):
        """min node
        """
        return self.__min(self.root)
    
    def __min(self,node):
        if node and node.left:
            return self.__min(node.left)
        else:
            return node
    
    def max(self):
        """max node
        """
        return self.__max(self.root)
    
    def __max(self,node):
        if node and node.right:
            return self.__max(node.right)
        else:
            return node
    
    def floor(self,key):
        """return the biggest node whose key is smaller than key
        """
        return self.__floor(self.root,key)

    def __floor(self,node,key):
        if not node:
            return None

        if node.key == key:
            return node
        if key < node.key:
            return self.__floor(node.left,key)
        tmp = self.__floor(node.right,key)
        if tmp:
            return tmp
        else:
            return node
    
    def ceil(self,key):
        """return the smallest node whose key is bigger than key
        """
        return self.__ceil(self.root,key)

    def __ceil(self,node,key):
        if not node:
            return None

        if node.key == key:
            return node
        if key > node.key:
            return self.__ceil(node.right,key)
        tmp = self.__ceil(node.left,key)
        if tmp:
            return tmp
        else:
            return node 

    def select(self,index):
        """return index's node
        """       
        return self.__select(self.root,index)
    
    def __select(self,node,index):
        if not node:
            return None
        
        num_left = self.__size(node.left)
        
        if num_left > index:
            return self.__select(node.left,index)
        elif num_left < index:
            return self.__select(node.right,index - num_left -1)
        else:
            return node
    
    def rank(self,key):
        """return the index of key
        """
        return self.__rank(self.root,key)
    
    def __rank(self,node,key):
        if not node:
            return 0
        if node.key == key:
            return self.__size(node.left)
        elif key < node.key:
            return self.__rank(node.left,key)
        else:
            return 1 + self.__size(node.left) + self.__rank(node.right,key)
    
    def deleteMin(self):
        """delete the minimum key node
        """
        self.root = self.__deleteMin(self.root)
    
    def __deleteMin(self,node):
        if not node.left:
            return node.right
        node.left = self.__deleteMin(node.left)
        node.N = self.__size(node.left) + self.__size(node.right) + 1
        return node
    
    def deleteMax(self):
        """delete the maxmium key node
        """
        self.root = self.__deleteMax(self.root)
    
    def __deleteMax(self,node):
        if not node.right:
            return node.left
        node.right = self.__deleteMax(node.right)
        node.N = self.__size(node.left) + self.__size(node.right) + 1
        return node
    
    def delete(self,key):
        """delete key node
        """
        self.root = self.__delete(self.root,key)
    
    def __delete(self,node,key):
        if not node:
            return None

        if key < node.key:
            node.left = self.__delete(node.left,key)
        elif key > node.key:
            node.right = self.__delete(node.right,key)
        else:
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            tmp = node
            node = self.__min(node.right)
            node.right = self.__deleteMin(tmp.right)
            node.left = tmp.left
        node.N = self.__size(node.left) + self.__size(node.right) + 1
        return node
        
    
if __name__ == "__main__":
    """simple test
    """
    import random
    bst = BST()
    print("Null BST size:",bst.size())
    list = []
    for index in range(0,100):
        list.append((index,index))
    random.shuffle(list)
    for index in range(100):
        bst.put(list[index][0],list[index][1])
    print("ABC BST size:",bst.size())
    bst.show()
    min_node =bst.min()
    print("Min: ",(min_node.key,min_node.value))
    max_node =bst.max()
    print("Max: ",(max_node.key,max_node.value))
    print("Floor 5 : ",(bst.floor(3).key))
    print("Ceil 17 : ",(bst.ceil(17).key))
    print('Select 19: ',(bst.select(19).key))    
    print('Rank 19: ',bst.rank(19))
    bst.deleteMin()
    min_node =bst.min()
    print("Min: ",(min_node.key,min_node.value))
    bst.deleteMax()
    max_node =bst.max()
    print("Max: ",(max_node.key,max_node.value))
    print("Delete 7")
    print('Rank 8',bst.rank(8))
    print('Rank 6',bst.rank(6))
    bst.delete(7)
    print('Rank 6',bst.rank(6))
    print('Rank 8',bst.rank(8))
    #bst.show()