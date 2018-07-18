
import numpy as np

class Graph(object):
    """
    邻接矩阵表示图
    """
    def __init__(self):
        self.vertexes = []
        self.edges = []

    def add_vertex(self, vertex):
        self.vertexes.append(vertex)

        if len(self.edges) > 0:
            tmp = self.edges
            size = len(self.vertexes)
            self.edges = np.zeros((size, size))
            for i in range(tmp.shape[0]):
                for j in range(tmp.shape[1]):
                    if tmp[i][j] == 1 : self.edges[i][j] = 1
        else:
            self.edges = np.zeros((len(self.vertexes), len(self.vertexes)))
    
    def add_edge(self, start_vertex, end_vertex):
        start_index = self.vertexes.index(start_vertex)
        end_index = self.vertexes.index(end_vertex)
        self.edges[start_index][end_index] = 1
        self.edges[end_index][start_index] = 1


g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')

print(g.vertexes)
print(g.edges)



