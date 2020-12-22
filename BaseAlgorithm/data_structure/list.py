# -*- coding: utf-8 -*-
"""
    List
    ~~~~~~~~~~~~~~

    make a list class. (Alought python has it's built-in list, 
    we will achieve this data structure by ourself. We will only
    use some basic functions of python so we can display the 
    details of list.)

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""
class Node:
        """Node

        Attributes:
            data : data
            next : quote of next Node
        """

        def __init__(self,init_data=None):
            self.__data = init_data
            self.__next = None
        
        def getData(self):
            """get the data in the node
            """
            return self.__data
        
        def getNext(self):
            """get the quota of next node
            """
            return self.__next
        
        def setData(self,new_data):
            """set data of this new node
            """
            self.__data = new_data
        
        def setNext(self,new_next):
            """set the quota of next data
            """
            self.__next = new_next


class List:
    """List of a object

    a simple demo of a list of a object

    Attributes:
        first : point to first node
    """
    
    def __init__(self):
        self.first = Node()

    def AddNodeOnHead(self,new_data):
        """Add a node on the head of the list
        """
        new_node = Node(new_data)
        new_node.setNext(self.first.getNext())
        self.first.setNext(new_node)
    
    def AddNodeOnEnd(self,new_data):
        """Add a node on the end of the end
        """
        node = self.first
        while node.getNext():
            node = node.getNext()
        #now node is the last node
        new_node = Node(new_data)
        node.setNext(new_node)
    
    def DeleteNodeOnHead(self):
        """delete a node on the head
        """
        if not self.isEmpty():
            next_node = self.first.getNext()
            self.first.setNext(next_node.getNext())
            next_node.setNext(None)
            del next_node
    
    def DeleteNodeOnEnd(self):
        """delete a node on the end
        """
        node = self.first
        if not self.isEmpty():
            while node.getNext().getNext():
                node = node.getNext()
            # now, node's next is the last
            last_node = node.getNext()
            node.setNext(None)
            del last_node
    
    def isEmpty(self):
        return self.first.getNext() == None
    
    def __next__(self):
        if self.current_node.getNext() == None:
            raise StopIteration
        else:
            self.current_node = self.current_node.getNext()
            return self.current_node
    
    def __iter__(self):
        #return first node
        self.current_node = self.first
        return self
    
if __name__ == '__main__':
    #this is a simple test example. [test pass]
    test_list = List()
    test_list.DeleteNodeOnHead()
    test_list.DeleteNodeOnEnd()
    for i in range(0,10):
        test_list.AddNodeOnEnd(i)
    test_list.DeleteNodeOnEnd()
    for i in range(0,10):
        test_list.AddNodeOnHead(i)
    test_list.DeleteNodeOnHead()
    for item in test_list:
        print(item.getData())
    