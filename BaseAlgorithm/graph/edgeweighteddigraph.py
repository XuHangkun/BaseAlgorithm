# -*- coding: utf-8 -*-
"""
    edge weighted directed graph
    ~~~~~~~~~~~~~~

    make a edge weighted directed graph class

    :copyright: (c) 2020 by Xu Hangkun.
    :license: LICENSE, see LICENSE for more details.
    :ref: [美]塞奇威克(Sedgewick, R.)，[美]韦恩(Wayne，K.).算法[M].北京:人民邮电出版社,2012.
"""
import queue
from BaseAlgorithm.search.binary_search_tree import BST
from BaseAlgorithm.graph.digraph import Topological,DirectedCircle

class DirectedEdge:
    """directed edge
    """

    def __init__(self,v:int,w:int,weight:float):
        self.__v = v
        self.__w = w
        self.__weight = weight
    
    def weight(self):
        return self.__weight
    
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
    
    def e_from(self):
        return self.__v
    
    def e_to(self):
        return self.__w
    
    def either(self):
        return self.__v

    def other(self,vertex):
        if vertex == self.__v:
            return self.__w
        elif vertex == self.__w:
            return self.__v
        else:
            return None 
    
    def __str__(self):
        return "%d -> %d %.2f"%(self.__v,self.__w,self.__weight)
    
class EdgeWeightedDiGraph:
    """edge weighted directed graph
    """
    def __init__(self,V=0):
        self.__v = V
        self.__e = 0
        self.__adj = []
        for index in range(self.__v):
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
                edge = DirectedEdge(int(tmp_edge[0]),int(tmp_edge[1]),float(tmp_edge[2]))
                if edge:
                    self.add_edge(edge)

    def add_edge(self,edge:DirectedEdge):
        """add a edge into the graph
        """
        self.__adj[edge.e_from()].append(edge)
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
    
    def edges(self):
        bag = []
        for i in range(self.__v):
            for j in self.adj(i):
                bag.append(j)
        return bag
    
    def show(self):
        """show the graph
        """
        print("Vertex Number: %d"%self.__v)
        print("Edge Number: %d"%self.__e)
        for index in range(self.__v):
            print("V %d"%index,self.adj(index))

class DijkstraSP:
    """generatre the smallest weighted path tree of a graph
    """
    
    def __init__(self,gr:EdgeWeightedDiGraph,s:int):
        self.__pq = BST()
        self.__edgeTo = []
        self.__distTo = []
        for index in range(gr.vertex_num()):
            self.__edgeTo.append(None)
            self.__distTo.append(float('inf'))
        self.__distTo[s] = 0
        self.__pq.put(s,self.__distTo[s])
        while not self.__pq.size()==0:
            min = self.__pq.min().key
            self.__pq.deleteMin()
            self.relax_edge(gr,min)
    
    def relax_edge(self,gr:EdgeWeightedDiGraph,v:int):
        for edge in gr.adj(v):
            w = edge.e_to()
            if self.__distTo[w] > (self.__distTo[v] + edge.weight()):
                self.__distTo[w] = self.__distTo[v] + edge.weight()
                self.__edgeTo[w] = edge
                self.__pq.put(w,self.__distTo[w])
    
    def relax_vertex(self,gr:EdgeWeightedDiGraph,v:int):
        for edge in gr.adj(v):
            w = edge.e_to()
            if self.__distTo[w] > (self.__distTo[v] + edge.weight()):
                self.__distTo[w] = self.__distTo[v] + edge.weight()
                self.__edgeTo[w] = edge
            
    
    def distTo(self,v:int):
        return self.__distTo[v]

    def hasPathTo(self,v:int):
        return self.__distTo[v] < float('inf')

    def pathTo(self,v:int):
        if not self.hasPathTo(v):
            return None
        
        path = []
        edge = self.__edgeTo[v]
        while edge.e_to != None:
            path.insert(0,edge)
            edge = self.__edgeTo[edge.e_from()]
        return path
    
    def edges(self):
        return self.__edgeTo


class AcyclicSP:
    """generatre the smallest weighted path tree of a acyclic graph
    """
    
    def __init__(self,gr:EdgeWeightedDiGraph,s:int):
        self.__edgeTo = []
        self.__distTo = []
        for index in range(gr.vertex_num()):
            self.__edgeTo.append(None)
            self.__distTo.append(float('inf'))
        self.__distTo[s] = 0
        
        top = Topological(EdgeWeightedDiGraph)
        for v in top.order():
            self.relax_vertex(gr,v)
    
    def relax_vertex(self,gr:EdgeWeightedDiGraph,v:int):
        for edge in gr.adj(v):
            w = edge.e_to()
            if self.__distTo[w] > (self.__distTo[v] + edge.weight()):
                self.__distTo[w] = self.__distTo[v] + edge.weight()
                self.__edgeTo[w] = edge
            
    
    def distTo(self,v:int):
        return self.__distTo[v]

    def hasPathTo(self,v:int):
        return self.__distTo[v] < float('inf')

    def pathTo(self,v:int):
        if not self.hasPathTo(v):
            return None
        
        path = []
        edge = self.__edgeTo[v]
        while edge.e_to != None:
            path.insert(0,edge)
            edge = self.__edgeTo[edge.e_from()]
        return path
    
    def edges(self):
        return self.__edgeTo

class EdgeWeightedDirectedCycle:
    """find cycle in a edge weighted cycle
    """
    def __init__(self,digr:EdgeWeightedDiGraph):
        self.__onStack = []
        self.__edgeTo = []
        self.__marked = []
        self.__circle = []
        for v in range(digr.vertex_num()):
            self.__onStack.append(False)
            self.__edgeTo.append(None)
            self.__marked.append(False)
        for v in range(digr.vertex_num()):
            if not self.__marked[v]:
                self.__dfs(digr,v)

    def __dfs(self,digr:EdgeWeightedDiGraph,v:int):
        self.__onStack[v] = True
        self.__marked[v] = True
        for w in digr.adj(v):
            if self.hasCircle():
                return
            elif not self.__marked[w]:
                self.__edgeTo[w] = v
                self.__dfs(digr,w)
            elif self.__onStack[w]:
                self.__circle = []
                x = v
                while x != w:
                    self.__circle.insert(0,x)
                    x = self.__edgeTo[x]
                self.__circle.insert(0,w)
                self.__circle.insert(0,v)
                return
        self.__onStack[v] = False
    
    def hasCircle(self):
        if self.__circle:
            return True
        else:
            return False
    
    def circle(self):
        return self.__circle

class BellmanFordSP:
    def __init__(self,gr:EdgeWeightedDiGraph,s:int):
        self.__edgeTo = []
        self.__distTo = []
        self.__onQ = []
        self.__queue = queue.Queue(0)
        self.__cost = 0
        self.__cycle = []
        for index in range(gr.vertex_num()):
            self.__edgeTo.append(None)
            self.__distTo.append(float('inf'))
            self.__onQ.append(False)
        self.__distTo[s] = 0
        self.__queue.put(s)
        self.__onQ[s] = True
        while not self.__queue.empty() and not self.hasNegativeCycle():
            v = self.__queue.get()
            self.__onQ[v] = False
            self.relax(gr,v)
        
    def findNegativeCycle(self):
        V = len(self.__edgeTo)
        spt = EdgeWeightedDiGraph(V)
        for v in range(V):
            if self.__edgeTo[v] != None:
                spt.add_edge(self.__edgeTo[v])
        
        cf = EdgeWeightedDirectedCycle(spt)
        self.__cycle = cf.circle()

    def hasNegativeCycle(self):
        self.__cycle != None
    
    def negativeCycle(self):
        return self.__cycle
    
    def relax(self,gr:EdgeWeightedDiGraph,v:int):
        for edge in gr.adj(v):
            w = edge.e_to()
            if self.__distTo[w] > (self.__distTo[v] + edge.weight()):
                self.__distTo[w] = self.__distTo[v] + edge.weight()
                self.__edgeTo[w] = edge
                if not self.__onQ[w]:
                    self.__onQ[w] = True
            self.__cost += 1
            if self.__cost % gr.vertex_num() == 0:
                self.findNegativeCycle()

    def distTo(self,v:int):
        return self.__distTo[v]

    def hasPathTo(self,v:int):
        return self.__distTo[v] < float('inf')

    def pathTo(self,v:int):
        if not self.hasPathTo(v):
            return None
        
        path = []
        edge = self.__edgeTo[v]
        while edge.e_to != None:
            path.insert(0,edge)
            edge = self.__edgeTo[edge.e_from()]
        return path
    
    def edges(self):
        return self.__edgeTo