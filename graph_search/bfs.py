import collections
import time

def bfs_list(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited

def bfs(graph, start):
    visited, queue = set(), collections.deque([start], maxlen=len(graph.keys()))
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited

if __name__ == '__main__':
    test_graph = {1: [2, 3, 4, 7],
             2: [1, 3, 4],
             3: [1, 2, 4],
             4: [1, 2, 3, 5],
             5: [4, 6, 7, 8],
             6: [5, 7, 8],
             7: [1, 5, 6, 8],
             8: [5, 6, 7]
             }
    print 'using list implementation'
    timer = time.time()
    print bfs_list(test_graph, 1)
    print time.time() - timer

    print 'using deque implementation'
    timer = time.time()
    print bfs(test_graph, 1)
    print time.time() - timer
