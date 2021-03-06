# -*- coding: utf-8 -*-
"""
    undirected graph
    ~~~~~~~~~~~~~~

    make a undirected graph class

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""

from BaseAlgorithm.search.binary_search_tree import BST
import queue

class Graph:
    """graph class
    """

    def __init__(self,V=0):
        """construction func
        """
        self.__v = V
        self.__e = 0
        self.__adj = []  #adjacency list
        for index in range(0,self.__v):
            self.__adj.append([])
    
    def load_graph(self,filename):
        """load graph from standard graph file

            standard graph file format
            line 1: 3        #number of vertex
            line 2: 2        #number of edge
            line 3: 1 2      #edge link vertex 1 and vertex 2
            line 4: ...
            ...
        """
        with open(filename,"r") as file:
            lines = file.readlines()
            self.__v = int(lines[0].strip('\n'))
            self.__e = 0
            self.__adj = []  #adjacency list
            for index in range(0,self.__v):
                self.__adj.append([])
            for line in lines[2:]:
                edge = line.split()
                if edge:
                    self.add_edge(int(edge[0]),int(edge[1]))

    def add_edge(self,v:int,w:int):
        """add a edge link vertex v and w
        """
        self.__adj[v].append(w)
        self.__adj[w].append(v)
        self.__e += 1
    
    def vertex_num(self):
        """number of vertexs
        """
        return self.__v
    
    def edge_num(self):
        """number of edges
        """
        return self.__e
    
    def adj(self,v:int):
        """return adjancent vertexs of vertex v
        """
        return self.__adj[v]
    
    def show(self):
        """show the graph
        """
        print("Vertex Number: %d"%self.__v)
        print("Edge Number: %d"%self.__e)
        for index in range(self.__v):
            print("V %d"%index,self.adj(index))

class SymbolGraph:
    """symbol graph
    """
    def __init__(self):
        """initialize the graph
        """
        self.__st = BST()  #symbol name -> index
        self.__keys = []
        self.__gr = Graph()
    
    def load_graph(self,filename,separator):
        """load graph from ASC file

        pars:
            filename: name of a file
                file format:
                A B
                B C
                C D
                ...
            separator: seperator between two connected vertices
                separator can be defined by yourself, like ',','.' and so on.
        """
        with open(filename,"r") as file:
            lines = file.readlines()
            for line in lines:
                edge = line.strip('\n').split(separator)
                for vertex in edge:
                    if not self.__st.contain(vertex):
                        self.__st.put(vertex,self.__st.size())

            for index in range(self.__st.size()):
                self.__keys.append("")

            for key in self.__st.keys():
                self.__keys[self.__st.get(key)] = key
            
            self.__gr = Graph(V=self.__st.size())
            for line in lines:
                edge = line.strip('\n').split(separator)
                if not edge:
                    continue
                v = self.__st.get(edge[0])
                for index in range(1,len(edge)):
                    self.__gr.add_edge(v,self.__st.get(edge[index]))
    
    def contains(self,key):
        """return True if graph contains key
        """
        return self.__st.contain(key)
    
    def index(self,key):
        """return index of key
        """
        return self.__st.get(key)
    
    def name(self,index):
        """return name of index
        """
        return self.__keys[index]
    
    def graph(self):
        """return graph
        """
        return self.__gr
    
    def show(self):
        """show the graph
        """
        print("Vertex Number: %d"%self.__gr.vertex_num())
        print("Edge Number: %d"%self.__gr.vertex_num())
        print("--------------------")
        for key in self.__st.keys():
            key_index = self.__st.get(key)
            if key_index != None:
                print(key+" :")
                key_adj_indexs = self.__gr.adj(self.__st.get(key))
                for adj in key_adj_indexs:
                    print("\t%s"%self.__keys[adj])

class DepthFirstPath:
    """use depth first to search graph
    """

    def __init__(self,gr:Graph,start:int):
        """
        """
        self.__marked = []
        self.__edgeTo = []
        self.__start = start
        for index in range(gr.vertex_num()):
            self.__marked.append(False)
            self.__edgeTo.append(None)
        self.__dfs(gr,start)

    def __dfs(self,gr:Graph,v:int):
        self.__marked[v] = True
        for vertex in gr.adj(v):
            if not self.__marked[vertex]:
                self.__edgeTo[vertex] = v
                self.__dfs(gr,vertex)
    
    def hasPathTo(self,vertex:int):
        """if vertex has path to start point
        """
        return self.__marked[vertex]

    def pathTo(self,vertex:int):
        """return the path from the vertex to start point
        """
        if not self.hasPathTo(vertex):
            return None
        
        path = []
        x = vertex
        while x != self.__start:
            path.insert(0,x)
            x = self.__edgeTo[x]
        
        path.insert(0,self.__start)
        return path

class BreadthFirstPaths:
    """use breadth first method to find path
    """
    def __init__(self,gr:Graph,start:int):
        """
        """
        self.__marked = []
        self.__edgeTo = []
        self.__start = start
        for index in range(gr.vertex_num()):
            self.__marked.append(False)
            self.__edgeTo.append(None)
        self.__bfs(gr,start)

    def __bfs(self,gr:Graph,start:int):
        que = queue.Queue(0)
        self.__marked[start] = True
        que.put(start)
        while not que.empty():
            v = que.get()
            for w in gr.adj(v):
                if not self.__marked[w]:
                    self.__edgeTo[w] = v
                    self.__marked[w] = True
                    que.put(w)
    
    def hasPathTo(self,vertex:int):
        """if vertex has path to start point
        """
        return self.__marked[vertex]

    def pathTo(self,vertex:int):
        """return the path from the vertex to start point
        """
        if not self.hasPathTo(vertex):
            return None
        
        path = []
        x = vertex
        while x != self.__start:
            path.insert(0,x)
            x = self.__edgeTo[x]
        
        path.insert(0,self.__start)
        return path

class CC:
    """find all connnected 
    """
    def __init__(self,gr:Graph):
        self.__marked = []
        self.__id = []
        self.__count=0
        for v in range(gr.vertex_num()):
            self.__marked.append(False)
            self.__id.append(None)
        
        for v in range(gr.vertex_num()):
            if not self.__marked[v]:
                self.__dfs(gr,v)
                self.__count += 1
            
    def __dfs(self,gr:Graph,v:int):
        self.__marked[v] = True
        self.__id[v] = self.__count
        for w in gr.adj(v):
            if not self.__marked[w]:
                self.__dfs(gr,w)
    
    def connected(self,v:int,w:int):
        return self.__id[v] == self.__id[w]

    def id(self,v:int):
        return self.__id[v]
    
    def count(self):
        return self.__count

if __name__ == "__main__":

    gr = Graph()
    gr.load_graph("graph.txt")
    print("show graph")
    gr.show()
    print("\n")

    #test path search class
    print("Test Path Search")
    for i in range(1,6):
        print("Path from 0 to %d"%i)
        dep = DepthFirstPath(gr,0)
        print("Depth First: ",dep.pathTo(i))
        bre = BreadthFirstPaths(gr,0)
        print("Breadth First: ",bre.pathTo(i))
    print("\n")

    #test cc
    print("Test Class CC")
    cc = CC(gr)
    print("Connect sub graph: ",cc.count())
    print("6 and 7",cc.connected(6,7))
    print("6 and 1",cc.connected(6,1))
    print("\n")

    symbol_gr = SymbolGraph()
    symbol_gr.load_graph("symbol_graph.txt",",")
    print("show symbol graph")
    symbol_gr.show()
    print("\n")