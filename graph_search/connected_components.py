import dfs
def dfs_connected(graph):
    connected_components = list()
    discovered_nodes = set()
    for node in graph.keys():
        if node not in discovered_nodes:
            connected = dfs.dfs(graph, node)
            connected_components.append(connected)
            discovered_nodes = discovered_nodes.union(connected)
            print 'connected_components', connected_components
            print 'discovered_nodes', discovered_nodes

    return connected_components

if __name__ == '__main__':

    disconnected_graph = {1: [2, 3, 4],
                          2: [1, 3, 4],
                          3: [1, 4, 2],
                          4: [1, 3, 2],
                          6: [7],
                          7: [6],
                          }

    print list(dfs_connected(disconnected_graph))
