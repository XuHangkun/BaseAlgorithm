# -*- coding: utf-8 -*-
"""
    search algrithms of string
    ~~~~~~~~~~~~~~

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""
class TrieSTNode:
    """node of
    """
    def __init__(self,value=None,R=256):
        #key should be comparable
        self.value = value
        self.next = []
        for i in range(R):
            self.next.append(None)

class TrieST:
    """search algrithms of string
    """

    def __init__(self,R=256):
        self.R = R
        self.root = None
    
    def get(self,key):
        """get value of key
        """
        x = self.__get(self.root,key,0)
        if x == None:
            return None
        return x.value
    
    def __get(self,node,key,d):
        if node == None:
            return None
        if d == len(key):
            return node
        c = ord(key[d])
        return self.__get(node.next[c],key,d+1)
    
    def put(self,key,value):
        self.root = self.__put(self.root,key,value,0)
    
    def __put(self,node,key,value,d):
        if node == None:
            node = TrieSTNode()
        
        if d == len(key):
            node.value = value
            return node

        c = ord(key[d])
        node.next[c] = self.__put(node.next[c],key,value,d+1)
        return node
            
    def keys(self):
        """return all strings in the tree
        """
        return self.keysWithPrefix("")
    
    def keysWithPrefix(self,pre):
        q = []
        self.collect(self.__get(self.root,pre,0),pre,q)
        return q
    
    def collect(self,node,pre,q):
        if node == None:
            return
        if node.value != None:
            q.append(pre)
        for c in range(self.R):
            self.collect(node.next[c],pre+chr(c),q)
    
    def keysThatMatch(self,pat):
        q = []
        self.pat_collect(self.root,"",pat,q)
        return q

    def pat_collect(self,node,pre,pat,q):
        d = len(pre)
        if node == None:
            return
        if d == len(pat) and node.value != None:
            q.append(pre)
        if d == len(pat):
            return

        next = pat[d]
        for c in range(self.R):
            if next == '.' or ord(next) == c:
                self.pat_collect(node.next[ord(next)],pre+chr(c),pat,q)

    def delete(self,key):
        self.root = self.__delete(self.root,key,0)
    
    def __delete(self,node,key,d):
        if node == None:
            return None
        if d == len(key):
            node.value = None
        else:
            c = ord(key[d])
            node.next[c] = self.__delete(node.next[c],key,d+1)

        if node.value != None:
            return node
        
        for c in range(self.R):
            if node.next[c] != None:
                return node
        return None