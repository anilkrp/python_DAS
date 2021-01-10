#!/usr/bin/env python
# coding: utf-8

# In[47]:


class Vertex:
    def __init__(self,n):
        self.name =n
        self.neighbor=list()
        
    def add_neighbor(self,v):
        if v not in self.neighbor:
            self.neighbor.append(v)
            self.neighbor.sort()
class Graph:
    
    vertices={}
    
    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name]=vertex
            return True
        else:
            return False
        
    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key , val in self.vertices.items():
                if key==u:
                    val.add_neighbor(v)
                elif key==v:
                    val.add_neighbor(u)
            return True
        else : 
            return False
        
    def printgraph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key+' '+str(self.vertices[key].neighbor))
        
            
g=Graph()
a=Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'),ord('K')):
    g.add_vertex(Vertex(chr(i)))
edges=['AB','AE','BF','CG','CA','DE','DH','EH','FG','FI','GJ','HI']
for j in edges:
    g.add_edge(j[:1],j[1:])
g.printgraph()


# In[72]:


class Vertex:
    def __init__(self,n):
        self.name = n
    
class Graph:
    vertices={}
    edges=[]
    edge_indices={}
    
    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name]=vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0]*(len(self.edges)+1))
            self.edge_indices[vertex.name]=len(self.edge_indices)
            return True
        else:
            return False
        
    def add_edge(self,u,v,weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]]=weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]]=weight
            return True
        else:
            False
            
    def print_graph(self): 
        print('*  A B C D E F G H I J')
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ',end=' ')
            for j in range(len(self.edges)):
                print(self.edges[i][j],end=' ')
            print(' ')
            
g=Graph()
a=Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'),ord('K')):
    g.add_vertex(Vertex(chr(i)))
ed=['AB','AE','BF','CG','CA','DE','DH','EH','FG','FI','GJ','HI']
for j in ed:
    g.add_edge(j[:1],j[1:])
g.print_graph()
    


# In[ ]:




