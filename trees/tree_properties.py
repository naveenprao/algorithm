import definition
codec = definition.Codec()
not_balanced = codec.deserialize('10 5 # 2 7 # # # #')
balanced = codec.deserialize('10 5 14 1 7 11 15 # # # # # # # #')
non_symmetric = codec.deserialize('10 5 5 3 7 3 7 # # # # # # # #')
symmetric = codec.deserialize('10 5 5 # 2 2 # # # # # # # # #')
def is_balanced(node):
    if node:
        l_height = is_balanced(node.left)
        r_height = is_balanced(node.right)
        print node.val, l_height, r_height
        if l_height > r_height:
            l_height, r_height = r_height, l_height
        assert( r_height-l_height <= 1)
        return r_height + 1

    else:
        return 0

def is_symmetric(node):
    def symmetricHelper(left, right):

        if not left and right:
            return False
        elif not right and left:
            return False
        elif not left and not right:
            return True
        else:
            return symmetricHelper(left.left, right.right) and symmetricHelper(left.right, right.left) and left.val == right.val

    if node:
        return symmetricHelper(node.left, node.right)
    else:
        return True

# expect error on unbalanced tree
try:
    is_balanced(not_balanced)
except AssertionError as ex:
    pass

# no error on balanced tree
is_balanced(balanced)

try:
    is_symmetric(not_balanced)
except AssertionError as ex:
    pass

print is_symmetric(balanced)
print is_symmetric(symmetric)
print is_symmetric(non_symmetric)