__author__ = 'nrao'

from collections import deque

from algorithm.datastructures import definition

codec = definition.Codec()
balanced_tree = codec.deserialize('10 5 14 1 7 11 15 # # # # # # # #')

class bst_iterator(object):
    def __init__(self, root):
        self.stk = deque()
        self.node = root

    def hasNext(self):
        if len(self.stk) or self.node:
            return True
        else:
            return False

    def getNext(self):
        val = None
        while len(self.stk) or self.node:
            if self.node:                # if node: push and go left
                self.stk.append(self.node)
                self.node = self.node.left
            else:                   # if null: pop, print, go right
                self.node = self.stk.pop()
                val = self.node.val
                self.node = self.node.right
                break

        return val

def iterative_inorder(node):
    stk = deque()
    while len(stk) or node:
        if node:                # if node: push and go left
            stk.append(node)
            node = node.left
        else:                   # if null: pop, print, go right
            node = stk.pop()
            print node.val
            node = node.right

iterative_inorder(balanced_tree)
it = bst_iterator(balanced_tree)
print it.getNext()
print it.getNext()
print it.hasNext()
for i in range(7):
    print it.getNext()
    print it.hasNext()
