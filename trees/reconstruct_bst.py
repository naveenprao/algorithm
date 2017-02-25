import definition
import sys
codec = definition.Codec()
MAX_INT = sys.maxint
MIN_INT = -sys.maxint - 1
def build_bst(pre_order):
    root_idx = [0]

    def helper(lower_bound, upper_bound):
        if root_idx[0] >= len(pre_order):
            return None

        root = pre_order[root_idx[0]]
        if root < lower_bound or root > upper_bound:
            return None

        root_idx[0] += 1
        left_subtree = helper(lower_bound, root)
        right_subtree = helper(root, upper_bound)
        return definition.TreeNode.init(root, left_subtree, right_subtree)

    return helper(MIN_INT, MAX_INT)

pre_order_node = [43, 23, 37, 29, 31, 41, 47, 53] 38

"""                                     43

                    23                          47

                              37                            53

                        29           41

                            31   38
"""

root = build_bst(pre_order_node)
print codec.serialize(root)
