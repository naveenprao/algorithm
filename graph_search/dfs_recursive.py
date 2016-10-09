import time

def dfs_recusive(graph, start):
    visited = set()

    def _dfs(node):
        visited.add(node)
        for next_node in set(graph[node]) - visited:
            _dfs(next_node)

    _dfs(start)
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

    print 'using recursive dfs implementation'
    timer = time.time()
    print dfs_recusive(test_graph, 1)
    print time.time() - timer
