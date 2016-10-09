
def kosaraju_ordering(graph):
    finish_order = [None]*10
    visited = set()
    counter = [1]

    def _dfs(node):
        if node not in visited:
            print 'visiting', node
            visited.add(node)
            for next_node in graph[node]:
                _dfs(next_node)

            print 'finished node', node, counter[0]
            finish_order[node] = counter[0]
            counter[0] += 1

    for start_node in graph:
        if start_node not in visited:
            print 'calling dfs using start node', start_node
            _dfs(start_node)

    return finish_order

def reverse_digraph(graph):
    reverse_graph = dict()

    for key in graph:
        reverse_graph[key] = set()

    print reverse_graph

    for node in graph:
        for connected_to in graph[node]:
            # s = reverse_graph[connected_to]
            # s.add(node)
            reverse_graph[connected_to].add(node)

    for key in reverse_graph.keys():
        reverse_graph[key] = list(reverse_graph[key])

    return reverse_graph

if __name__ == '__main__':
    di_graph = {1: [4],
                2: [8],
                3: [6],
                4: [7],
                5: [2],
                6: [9],
                7: [1],
                8: [6, 5],
                9: [7, 3]}

    # try:

    print di_graph
    reverse_graph = reverse_digraph(di_graph)
    print reverse_graph

    kosaraju_order = kosaraju_ordering(reverse_graph)
    print kosaraju_order
