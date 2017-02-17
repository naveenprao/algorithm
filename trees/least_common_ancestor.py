import definition
codec = definition.Codec()
balanced_tree = codec.deserialize('10 5 14 1 7 11 15 # # # # # # # #')

def find_search_path(root, search_val):
    found = [False]

    def search_helper(node):
        if found[0] is True or not node:
            return
        if node.val == search_val:
            found[0] = True
            return

        search_helper(node.left)
        search_helper(node.right)

    search_helper(root)
    return found

print find_search_path(balanced_tree, 16)
