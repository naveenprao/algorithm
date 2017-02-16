import unittest
from priority_queue import PriorityQueue
import sys

class Dijkstra(object):
    def __init__(self, graph):
        self.graph = graph

    def getShortestPathFrom(self, source):
        pq = PriorityQueue()
        dist_from_source = {}
        path_from_source = {}
        for key in self.graph.keys():
        # initialize the pq with vertices and their di
            if key is source:
                pq.add_item(key, 0)
            else:
                pq.add_item(key, sys.maxint)
            path_from_source[key] = []

        try:
            while True:
                dist, vertex = pq.pop_item()
                dist_from_source[vertex] = dist
                for conn_vertex in self.graph[vertex].keys():
                    if pq.peek_priority(conn_vertex) > dist + self.graph[vertex][conn_vertex]:
                        path_from_source[conn_vertex] = path_from_source[vertex][:] + [vertex]
                        pq.add_item(conn_vertex, min(pq.peek_priority(conn_vertex), dist + self.graph[vertex][conn_vertex]))
        except KeyError:
            pass

        return dist_from_source, path_from_source

class TestDijkstra(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = {'s': {'v': 1, 'w': 4},
                     'v': {'t': 6, 'w': 2},
                     'w': {'t': 3},
                     't': {},
                     }

    def test_simple_graph(self):
        d = Dijkstra(self.graph)
        dist, path = d.getShortestPathFrom('s')
        print dist
        print path


if __name__ == '__main__':
    unittest.main()

4, 1, 3, 2, 3
0, 1, 2, 3, 4
0, 1, 1, 2, 1
POS - 0, 0, 1, 3, 4

0, 1, 2, 3, 4
1, 2, 3, 3, 4