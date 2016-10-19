class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.data = None

    @classmethod
    def init_with_data(cls, data):
        obj = cls()
        obj.data = data
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

    @staticmethod
    def right_rotate(node):
        # if the node (to rotate) or its right child is none, we return.
        if node is None or node.right is None:
            return node

        x = node
        y = node.right

        # Consider A as x's left subtree
        # B as y's left subtree and
        # C as y's right subtree
        B = y.left

        # Perform the rotation
        y.left = x
        y.parent = x.parent
        x.parent = y

        x.right = B
        if B is not None:
            B.parent = x

        return y

    @staticmethod
    def left_rotate(node):
        # if node (to rotate) or its left child is none return
        if node is None or node.left is None:
            return node

        x = node
        y = node.left

        # Consider x right subtree as C
        # y's left subtree as A and right subtree as B
        B = y.right

        # perform the rotation
        y.right = x
        y.parent = x.parent
        x.parent = y

        x.left = B
        if B is not None:
            B.parent = x

        return y

    def display_tree(self):
        BST.display(self.root)

    @staticmethod
    def display(current_node, depth=0):
        if current_node is not None:
            BST.display(current_node.right, depth+1)
            print '\t' * depth, current_node.data
            BST.display(current_node.left, depth+1)

    def successor(self, node):
        if node is None:
            return None

        def _find_desendent(cur_node):
            while cur_node.left is not None:
                cur_node = cur_node.left
            return cur_node

        def _find_ancestor(cur_node):
            while cur_node is not None and cur_node.parent is not None and cur_node.parent.right == cur_node:
                cur_node = cur_node.parent

            if cur_node.parent is None:
                return node
            if cur_node.parent.left == cur_node:
                return cur_node.parent

        if node.right is None:
            return _find_ancestor(node)
        else:
            return _find_desendent(node.right)

    def predecessor(self, node):
        if node is None:
            return None

        def _find_ancestor(cur_node):
            while cur_node is not None and cur_node.parent is not None and cur_node.parent.left == cur_node:
                cur_node = cur_node.parent

            if cur_node.parent is None:
                return node
            if cur_node.parent.right == cur_node:
                return cur_node.parent

        def _find_decendent(cur_node):
            while cur_node.right is not None:
                cur_node = cur_node.right
            return cur_node

        if node.left is None:
            return _find_ancestor(node)
        else:
            return _find_decendent(node.left)

    def delete(self, data):
        node_to_del = self.root
        while node_to_del is not None and node_to_del.data != data:
            if data < node_to_del.data:
                node_to_del = node_to_del.left
            if data > node_to_del.data:
                node_to_del = node_to_del.right

        if node_to_del is None:
            raise ValueError("BST doesn't have data")

        def _delete(cur_node):
            # leaf node
            if cur_node.left is None and cur_node.right is None:
                if cur_node.parent.left == cur_node:
                    cur_node.parent.left = None
                else:
                    cur_node.parent.right = None
                return

            # Node with only one child case
            if cur_node.left is None:
                if cur_node.parent.left == cur_node:
                    cur_node.parent.left = cur_node.right
                else:
                    cur_node.parent.right = cur_node.right
                # reassign parent of subtree
                cur_node.right.parent = cur_node.parent
                return

            elif cur_node.right is None:
                if cur_node.parent.left == cur_node:
                    cur_node.parent.left = cur_node.left
                else:
                    cur_node.parent.right = cur_node.right
                # reassign parent of subtree
                cur_node.left.parent = cur_node.parent
                return

            # Node with both children
            if cur_node.left is not Node and cur_node.right is not None:
                pred = self.predecessor(cur_node)
                cur_node.data, pred.data = pred.data, cur_node.data
                _delete(pred)

        _delete(node_to_del)

if __name__ == '__main__':
    bst = BST.init_with_list(Node.init_with_list([3, 1, 5, 0, 2, 7, 4]))
    bst.display_tree()

    list_bst = BST.init_with_list(Node.init_with_list([0, 1, 3, 4, 5, 6, 7]))
    list_bst.display_tree()

    for i in range(3):
        list_bst.root = BST.right_rotate(list_bst.root)
    list_bst.root.right = BST.right_rotate(list_bst.root.right)
    list_bst.display_tree()

    list_bst.root.left = BST.left_rotate(list_bst.root.left)
    list_bst.display_tree()

    successor = list_bst.successor(list_bst.root.right.right)
    print 'successor', successor.data

    pred = list_bst.predecessor(list_bst.root.right)
    print 'pred', pred.data

    simple_bst = BST.init_with_list(Node.init_with_list([4, 1, 6, 0, 3, 5, 7]))
    simple_bst.display_tree()
    simple_bst.delete(6)
    simple_bst.delete(1)
    simple_bst.display_tree()
