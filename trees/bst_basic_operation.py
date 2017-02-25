__author__ = 'nrao'
"""                                     43

                    23                          47

                              37                            53

                        29           41

                            31   38
"""

"""
Insert :  Search in bst and insert as leaf

Delete :
1. Leaf Case: delete it.

2. Internal Node with one child
    Replace node with child node.

3. Internal node with two children
    a. find predecessor/successor
    b. Pred/succ can only have left/right child respectively. delete pred/succ
    c. Replace node with predecessor/successor

"""
