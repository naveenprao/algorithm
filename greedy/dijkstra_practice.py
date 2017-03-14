import sys

from algorithm.datastructures import priority_queue

graph = {'s': {'v': 1, 'w': 4},
         'v': {'t': 6, 'w': 2},
         'w': {'t': 3},
         't': {},
         }

def find_shortest_path(source):
    shortestPath = {}
    shortestDist = {}
    pq = priority_queue.PriorityQueue()
    for node in graph.keys():
        if node == source:
            pq.add_item(node, 0)
        else:
            pq.add_item(node, sys.maxint)
        shortestPath[node] = []

    while True:
        try:
            weight, node = pq.pop_item()
            shortestDist[node] = weight
            for edge in graph[node].keys():
                if pq.peek_priority(edge) > weight + graph[node][edge]:
                    pq.add_item(edge, weight+graph[node][edge])
                    shortestPath[edge] = shortestPath[node][:]+[node]
        except KeyError:
            break

    print shortestDist
    print shortestPath


def find_spanning_tree(source):
    pq = priority_queue.PriorityQueue()
    spanning_tree = list()
    for vertex in graph.keys():
        if vertex == source:
            pq.add_item(vertex, 0)
        else:
            pq.add_item(vertex, sys.maxint)

    print pq.entry_finder
    try:
        while True:
            distance, node = pq.pop_item()
            print pq.entry_finder
            spanning_tree.append(node)
            for conn in graph[node].keys():
                if pq.peek_priority(conn) > graph[node][conn]:
                    pq.add_item(conn, graph[node][conn])
    except KeyError:
        pass

    print spanning_tree

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


find_shortest_path('s')
find_spanning_tree('s')
bellman_ford('s')
