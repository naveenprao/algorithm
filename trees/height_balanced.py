import definition
codec = definition.Codec()
root = codec.deserialize('10 5 # 2 7 # # # #')

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

is_balanced(root)
