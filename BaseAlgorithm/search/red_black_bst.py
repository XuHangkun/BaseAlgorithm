# -*- coding: utf-8 -*-
"""
    red black binary search tree
    ~~~~~~~~~~~~~~

    make a red black binary search binary search tree class

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""

class RedBlackNode:
    """node of red black binary search tree
    """
    RED = True
    BLACK = False
    def __init__(self,key=None,value=None,N=0,left=None,right=None,color=RedBlackNode.BLACK):
        #key should be comparable
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.N = N
        self.color = color

class RedBlackBST:
    """red black binary search
    """
    def __init__(self):
        self.root = None
    
    def __isRed(self,node):
        """judge if the link which linked to the node is red
        """
        if not node:
            return False
        return node.color == RedBlackNode.RED

    def size(self):
        """get size of RedBlackBST
        """
        return self.__size(self.root)

    def __size(self,node):
        if not node:
            return 0
        else:
            return node.N
    
    def __rotateLeft(self,node):
        """rotate the right link to the left
        """
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RedBlackNode.RED
        x.N = node.N
        node.N = 1 + self.__size(node.left) + self.__size(node.right)
        return x
    
    def __rotateRight(self,node):
        """rotate the left link to left 
        """
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = RedBlackNode.RED
        x.N = node.N
        node.N = 1 + self.__size(node.left) + self.__size(node.right)
        return x
    
    def __flipColors(self,node):
        """flip colors when both left and right link of node is red
        """
        node.color = RedBlackNode.RED
        node.left.color = RedBlackNode.BLACK
        node.right.color = RedBlackNode.BLACK
    
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
        """put (key,value) into the tree
        """
        self.root = self.__put(self.root,key,value)
    
    def __put(self,node,key,value):
        """
        """
        if not node:
            return RedBlackNode(key=key,value=value,N=1,color=RedBlackNode.RED)
        
        if key < node.key :
            node.left = self.__put(node.left,key,value)
        elif key > node.key :
            node.right = self.__put(node.right,key,value)
        else:
            node.value == value
        
        if self.__isRed(node.right) and not self.__isRed(node.left):
            node = self.__rotateLeft(node)

        if self.__isRed(node.left) and self.__isRed(node.left.left):
            node = self.__rotateRight(node.right)
        
        if self.__isRed(node.right) and self.__isRed(node.left):
            self.__flipColors(node)
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
    
    