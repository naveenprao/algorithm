__author__ = 'nrao'
l = [10, 20, 30, 40, 50, 60]
p = [2, 0, 1, 3, 5, 4]
nxt = 2
"""
p[0] = 2
b = 30
10, 20, 10, 40
-2, 0, 1, 3

p[2] = 1
b = 20
10, 30, 10, 40

p[1] = 0
b = 10
20, 30, 10, 40
-2, -0, 1, 3

"""

def apply_permutation(l, p):
    """
    Apply permutation using additional memory for flags
    :param l: input array
    :param p: permutation array
    :return: modified array
    """

    for i in xrange(len(l)):
        nxt = i
        print 'change - ', i
        while p[nxt] >= 0:
            print 'before-', i, p[nxt], l, p

            l[i], l[p[nxt]] = l[p[nxt]], l[i]
            temp = p[nxt]
            p[nxt] -= len(p)
            nxt = temp
            print 'after -', i, p[nxt], l, p


    print l

apply_permutation(l, p)