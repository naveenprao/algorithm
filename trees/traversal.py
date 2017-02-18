import definition
from collections import deque
codec = definition.Codec()
balanced_tree = codec.deserialize('10 5 14 1 7 11 15 # # # # # # # #')

"""
        10

    5       14

 1     7  11   15
"""
def find_search_path(root, search_val):
    found = [False]
    search_path = deque()

    def search_helper():
        while found[0] is False and search_path:
            node = search_path.pop()
            if node and node.val == search_val:
                found[0] = True
                return
            else:
                if node.right:
                    search_path.append(node.right)
                if node.left:
                    search_path.append(node.left)

    search_path.append(root)
    search_helper()
    for node in search_path:
        print node.val
    return found

def iterative_preorder(node):
    if not node:
        return
    stk = deque()
    stk.append(node)
    while len(stk):
        nd = stk.pop()
        print nd.val
        if nd.left:
            stk.append(nd.right)
        if nd.right:
            stk.append(nd.left)

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

def iterative_postorder(node):
    stk = deque()
    last_processed = None
    while len(stk) or node:
        if node:
            stk.append(node)
            node = node.left
        else:
            peekNode = stk[len(stk)-1]
            # if right child exists and traversing node from left child, move right
            if peekNode.right and last_processed != peekNode.right:
                node = peekNode.right
            else:
                print peekNode.val
                last_processed = stk.pop()

def iterative_postorder_twostack(node):
    stk = deque()
    stk.append(node)
    ans_stk = deque()
    while len(stk):
        node = stk.pop()
        ans_stk.appendleft(node.val)
        if node.left:
            stk.append(node.left)
        if node.right:
            stk.append(node.right)

    for ans in ans_stk:
        print ans

# iterative_preorder(balanced_tree)
# iterative_inorder(balanced_tree)
# iterative_postorder(balanced_tree)
iterative_postorder_twostack(balanced_tree)