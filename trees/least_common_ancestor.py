# Ref : http://articles.leetcode.com/lowest-common-ancestor-of-a-binary-tree-part-i/
from algorithm.datastructures import definition

codec = definition.Codec()
balanced_tree = codec.deserialize('10 5 14 1 7 11 15 # # # # # # # #')

"""
        10

    5       14

 1     7  11   15
"""
def count_matches(node, p, q):
    if not node:
        return 0
    match = count_matches(node.left, p, q) + count_matches(node.right, p, q)
    if node.val == p or node.val == q:
        return 1 + match
    else:
        return match

def find_lca_topdown(root, p, q):
    if not root or not p or not q:
        return None
    if root.val == p or root.val == q:
        return root
    match = count_matches(root.left, p, q)
    if match == 1:
        return root
    elif match == 2:
        return find_lca_topdown(root.left, p, q)
    else:
        return find_lca_topdown(root.right, p, q)

def find_lca_bottomup(root, p, q):
    if not root:
        return None
    if root.val == p or root.val == q:
        return root
    l = find_lca_bottomup(root.left, p, q)
    r = find_lca_bottomup(root.right, p, q)
    if l and r:
        return root
    elif l:
        return l
    else:
        return r

# TODO: fix missing node case
lca = find_lca_topdown(balanced_tree, 15, 11)
print lca.val

lca = find_lca_bottomup(balanced_tree, 1, 15)
print lca.val
