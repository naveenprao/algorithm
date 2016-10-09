import time
import collections


def topo(graph):
    visited = set()
    topo_sorted = collections.deque(maxlen=len(graph.keys()))
    lable = {}

    def _dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor in visited and lable.get(neighbor, '') == 'start':
                raise Exception('cycle found')
        for next_node in set(graph[node]) - visited:
            lable[next_node] = 'start'
            _dfs(next_node)
        topo_sorted.appendleft(node)
        lable[node] = 'end'

    for node in graph.keys():
        if node not in visited:
            lable[node] = 'start'
            _dfs(node)

    return topo_sorted


if __name__ == '__main__':
    di_graph = {0: [],
                1: [],
                2: [3],
                3: [1],
                4: [0],
                5: [0, 2],
                6: [7],
                8: [9],
                7: [8],
                9: []
                }

    print 'using recursive dfs implementation'
    timer = time.time()
    try:
        topo_order = topo(di_graph)
        print list(topo_order)
    except Exception:
        print "topo order cannot be calculated if there's a cycle"
        raise
    finally:
        print time.time() - timer
