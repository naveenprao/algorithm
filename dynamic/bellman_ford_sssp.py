__author__ = 'nrao'

import sys
graph = {'s': {'v': 1, 'w': 4},
         'v': {'t': 6, 'w': 2},
         'w': {'t': 3},
         't': {},
         }

def bellman_ford(source):
    shortest_path = {}
    for node in graph.keys():
        if node == source:
            shortest_path[node] = 0
        else:
            shortest_path[node] = sys.maxint

    for i in range(len(graph.keys())-1):
        for node in graph.keys():
            for out_node in graph[node].keys():
                if shortest_path[out_node] > shortest_path[node] + graph[node][out_node]:
                    shortest_path[out_node] = shortest_path[node] + graph[node][out_node]

    print shortest_path

bellman_ford('s')
