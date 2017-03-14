__author__ = 'nrao'
from algorithm.datastructures.union_find import UnionFind

graph = {'s': {'v': 1, 'w': 4},
         'v': {'t': 6, 'w': 2},
         'w': {'t': 3},
         't': {},
         }


def kruskals_mst(s):
    # sort edges based on weight
    edges = list()
    mst = list()
    for start in graph.keys():
        for end in graph[start].keys():
            edges.append((graph[start][end], start, end))
    edges = sorted(edges)
    print edges
    uf = UnionFind()

    st_idx, en_idx = 1, 2
    for e in edges:
        if uf[e[st_idx]] != uf[e[en_idx]]:
            mst.append((e[st_idx], e[en_idx]))
            uf.union(e[st_idx], e[en_idx])

    print mst

kruskals_mst('s')
