# -*- coding: utf-8 -*-
"""
    edge weighted undirected graph
    ~~~~~~~~~~~~~~

    make a edge weighted undirected graph class

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""
import queue
from BaseAlgorithm.search.binary_search_tree import BST

class Edge:
    """weighted edge
    """
    def __init__(self,v:int,w:int,weight:float):
        self.__v = v
        self.__w = w
        self.__weight = weight
    
    def weight(self):
        return self.__weight

    def either(self):
        return self.__v

    def other(self,vertex):
        if vertex == self.__v:
            return self.__w
        elif vertex == self.__w:
            return self.__v
        else:
            return None

    def __lt__(self,edge):
        return self.__weight < edge.__weight

    def __le__(self,edge):
        return self.__weight <= edge.__weight
    
    def __gt__(self,edge):
        return self.__weight > edge.__weight

    def __ge__(self,edge):
        return self.__weight >= edge.__weight

    def __eq__(self,edge):
        return self.__weight == edge.__weight

    def __ne__(self,edge):
        return self.__weight != edge.__weight

    def show(self):
        return "%d-%d %.2f"%(self.__v,self.__w,self.__weight)
        
class EdgeWeightedGraph:
    """edge weighted graph
    """
    
    def __init__(self,V=0):
        self.__v = V
        self.__e = 0
        self.__adj = []  #adjacency list
        for index in range(0,self.__v):
            self.__adj.append([])
    
    def load_graph(self,filename):
        """load graph from standard graph file

            standard graph file format
            line 1: 3           #number of vertex
            line 2: 2           #number of edge
            line 3: 1 2 0.1     #edge link vertex 1 and vertex 2
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
                tmp_edge = line.split()
                edge = Edge(int(tmp_edge[0]),int(tmp_edge[1]),float(tmp_edge[2]))
                if edge:
                    self.add_edge(edge)

    def add_edge(self,e:Edge):
        """add a edge link vertex
        """
        v = e.either()
        w = e.other(v)
        self.__adj[v].append(e)
        self.__adj[w].append(e)
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

class PrimMST:
    """generate minimum spanning tree in prim algorithm
    """
    def __init__(self,gr):
        self.__pq = BST()
        self.__marked = []
        self.__mst = queue.Queue(0)

        for index in range(gr.vertex_num()):
            self.__marked.append(False)   

        self.__visit(gr,0)
        while not self.__pq.size() == 0 :
            edge = self.__pq.min().value
            self.__pq.deleteMin()

            v = edge.either()
            w = edge.other(v)
            if self.__marked[v] and self.__marked[w]:
                continue

            self.__mst.put(edge)
            
            if not self.__marked[v]:
                self.__visit(gr,v)
            if not self.__marked[w]:
                self.__visit(gr,w)
                
    def __visit(self,gr:EdgeWeightedGraph,v:int):
        self.__marked[v] = True
        for edge in gr.adj(v):
            if not self.__marked[edge.other(v)]:
                key = "%d-%d"%(v,edge.other(v))
                self.__pq.put(key,edge)
    
    def mst(self):
        """return the mst
        """
        return self.__mst

if __name__ == "__main__":
    gr = EdgeWeightedGraph()
    gr.load_graph("tinyEWG.txt")
    prim_mst = PrimMST(gr)
    print(prim_mst.mst().empty())