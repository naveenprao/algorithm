import sys

from algorithm.datastructures import priority_queue

graph = {'s': {'v': 1, 'w': 4},
         'v': {'t': 6, 'w': 2},
         'w': {'t': 3},
         't': {},
         }

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

find_spanning_tree('s')