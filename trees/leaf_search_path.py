__author__ = 'nrao'
import definition
from collections import deque

codec = definition.Codec()
not_balanced = codec.deserialize('10 5 # 2 7 # # # #')
balanced = codec.deserialize('10 5 14 1 7 11 15 # # # # # # # #')

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

    def helper(node, total):
        if not node:
            return 0

        total = total + node.val
        if not node.left and not node.right:
            return total
        else:
            return helper(node.left, total) + helper(node.right, total)

    return helper(root, 0)

leaf_path(balanced)
print sum_leaf_path(balanced)