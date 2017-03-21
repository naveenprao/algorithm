from algorithm.datastructures import definition
from collections import deque
codec = definition.Codec()
balanced = codec.deserialize('10 5 14 1 7 11 15 # # # # # # # #')

def print_bfs(root):
    dq = deque()

    def _builder(q):
        nodes = [n.val for n in q]
        print nodes

        if not q:
            return

        new_level = deque()
        for node in q:
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)
        _builder(new_level)

    dq.append(root)
    _builder(dq)

def right_sibling_tree(nd):
    sibling = dict()

    def populate_lower_level(node):
        while node:
            sibling[node.left] = node.right              # simulate the sibling link
            print node.left.val, node.right.val

            if node in sibling:
                sibling[node.right] = sibling[node].left
                print node.right.val, sibling[node].left.val
                node = sibling[node]
            else:
                break

    while nd and nd.left:
        populate_lower_level(nd)
        nd = nd.left

assert(a)
right_sibling_tree(balanced)