__author__ = 'nrao'
from collections import deque

from algorithm.datastructures import definition

codec = definition.Codec()
not_balanced = codec.deserialize('10 5 # 2 7 # # # #')
balanced = codec.deserialize('10 5 14 1 7 11 15 # # # # # # # #')

decemal = codec.deserialize('1 2 3 4 5 6 7 # # # # # # # #')
def leaf_path(root):
    stk = deque()

    def helper(node):
        if node:
            stk.append(node)
        else:
            return

        if not node.left and not node.right:
            print [x.val for x in stk]

        helper(node.left)
        helper(node.right)

        stk.pop()

    if not root:
        return
    helper(root)

def sum_leaf_path(root):

    def helper(node):
        if not node:
            return 0

        return node.val + helper(node.left) + helper(node.right)

    return helper(root)

def path_sum(root, base):

    def _helper(node, sum):
        if not node:
            return 0
        partial_sum = sum * base + node.val
        if not node.left and not node.right:
            return partial_sum
        else:
            return _helper(node.left, partial_sum) + _helper(node.right, partial_sum)

    return _helper(root, 0)

leaf_path(balanced)
print sum_leaf_path(balanced)
print path_sum(decemal, 10)
