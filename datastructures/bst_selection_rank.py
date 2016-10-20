import unittest

class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.data = None
        self.population = None

    @classmethod
    def init_with_data(cls, data):
        obj = cls()
        obj.data = data
        obj.population = 1
        return obj

    @staticmethod
    def init_with_list(list_of_node):
        node_list = list()
        for data in list_of_node:
            node_list.append(Node.init_with_data(data))
        return node_list

class BST(object):
    def __init__(self):
        self.root = None

    @classmethod
    def init_with_root(cls, node):
        obj = cls()
        obj.root = node
        return obj

    @classmethod
    def init_with_list(cls, node_list):
        obj = cls()
        for node in node_list:
            obj.insert(node)

        return obj

    def insert(self, node):
        if self.root is None:
            self.root = node
            return

        parent_node = self.root
        while True:
            if parent_node.data < node.data:
                if parent_node.right is not None:
                    parent_node = parent_node.right
                else:
                    parent_node.right = node
                    node.parent = parent_node
                    break
            elif parent_node.data > node.data:
                if parent_node.left is not None:
                    parent_node = parent_node.left
                else:
                    parent_node.left = node
                    node.parent = parent_node
                    break
            elif parent_node.data == node.data:
                raise ValueError("data already in BST %s" % node.data)

        while parent_node is not None:
            parent_node.population += 1
            parent_node = parent_node.parent

    def display_tree(self):
        BST.display(self.root)

    @staticmethod
    def display(current_node, depth=0):
        if current_node is not None:
            BST.display(current_node.right, depth+1)
            print '\t' * depth, '%d(%d)' % (current_node.data,current_node.population)
            BST.display(current_node.left, depth+1)

    def select(self, index):
        if self.root is None or index > self.root.population:
            raise ValueError("BST doesn't contain %d elements"%index)

        def _select(cur_index, cur_node):
            # print 'cur_index', cur_index
            leftPop = 0
            if cur_node.left is not None:
                leftPop += cur_node.left.population
            if cur_index == leftPop + 1:
                return cur_node.data

            if cur_node.left is not None and cur_node.left.population >= cur_index:
                return _select(cur_index, cur_node.left)
            elif cur_node.right is not None:
                return _select(cur_index - (cur_node.left.population + 1), cur_node.right)

        return _select(index, self.root)

    def rank(self, data):
        node = self.root
        rank = 0
        while node is not None:
            if data > node.data:
                rank += (node.population - node.left.population)
                node = node.right
            elif data < node.data:
                node = node.left
            elif data == node.data:
                rank += 1
                break

        if node == None:
            raise ValueError("Node with data:%d not found" % data)

        return rank


class Test_BST(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bst = BST.init_with_list(Node.init_with_list([3, 1, 5, 0, 2, 7, 4]))
        cls.bst.display_tree()

    def test_rank(self):
        self.assertTrue(self.bst.select(1) == 0)
        self.assertTrue(self.bst.select(2) == 1)
        self.assertTrue(self.bst.select(3) == 2)
        self.assertTrue(self.bst.select(4) == 3)
        self.assertTrue(self.bst.select(5) == 4)
        self.assertTrue(self.bst.select(6) == 5)
        self.assertTrue(self.bst.select(7) == 7)

    def test_selection(self):
        rank = self.bst.rank(5)
        self.assertTrue(rank == 5, "expected %d actual %d" % (5, rank))
        self.assertTrue(self.bst.rank(7) == 7)
        self.assertTrue(self.bst.rank(4) == 5)
if __name__ == '__main__':
    unittest.main()
