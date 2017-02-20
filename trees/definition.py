__author__ = 'nrao'
from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def init(cls, val, left, right):
        instance = cls(val)
        instance.left = left
        instance.right = right
        return instance

# Serialize and deserialize utility
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string

        :param root: TreeNode
        :return:str
        """
        def serializeHelper():
            while len(queue):
                node = queue.popleft()
                if not node:
                    vals.append('#')
                else:
                    vals.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)

        vals = list()
        queue = deque()
        queue.append(root)
        serializeHelper()
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree

        :param data: str
        :return: TreeNode
        """
        def getNode():
            val = next(vals)
            if val == '#':
                return None
            else:
                return TreeNode(int(val))

        def deserializeHelper():
            while len(queue):
                node = queue.popleft()
                node.left = getNode()
                if node.left:
                    queue.append(node.left)
                node.right = getNode()
                if node.right:
                    queue.append(node.right)

        def _split(source, sep):
            sepsize = len(sep)
            start = 0
            while True:
                idx = source.find(sep, start)
                if idx == -1:
                    yield source[start:]
                    return
                yield source[start:idx]
                start = idx+sepsize

        vals = iter(_split(data, ' '))
        root = getNode()
        queue = deque()
        queue.append(root)
        deserializeHelper()
        return root


if __name__ == '__main__':
    r = TreeNode(10)
    r.left = TreeNode(5)
    r.right = TreeNode(14)
    r.left.left = TreeNode(1)
    r.left.right = TreeNode(7)

    codec = Codec()
    tree_data = codec.serialize(r)
    assert tree_data == '10 5 14 1 7 # # # # # #'

    newRoot = codec.deserialize(tree_data)
    newData = codec.serialize(newRoot)
    print newData