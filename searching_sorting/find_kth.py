def find_kth(A, B, k):
    # Stopping condition is when only k elements are left in both the array
    # return the max of the last elements
    if len(A) > len(B):
        A, B = B, A
    if not A:
        return B[k]
    if len(A) + len(B) - 1 == k:
        return max(A[-1], B[-1])

    # invariant k = i + j
    # set i to be k/2 whenever possible; this way we at least eliminate k/2 elements in each cycle.
    i = min(len(A)-1, k/2)
    j = min(len(B)-1, k-i)

    # if A[i] is greater; at least i elements from A is in the set of k-smallest elements.
    # similarly if B[j] is greater; at least j elements from B are in the set of k-smallest elements.
    # so remove them and reduce k accordingly and recursively call find_kth.
    if A[i] > B[j]:
        return find_kth(A[:i], B[j:], i)
    else:
        return find_kth(A[i:], B[:j], j)

A = [0, 2, 4, 6, 8, 10]
B = [1, 3, 5, 7, 9, 11]
k = find_kth(A, B, 5)

print "kth smallest:", k