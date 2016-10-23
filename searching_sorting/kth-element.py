import unittest


class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        return self.findKth(A, B, l // 2) if l % 2 == 1 else (self.findKth(A, B, l // 2 - 1) + self.findKth(A, B,
                                                                                                            l // 2)) / 2.0

    def findKth(self, A, B, k):
        print 'A, B, k', A, B, k
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])

        i = min(len(A)-1, k/2)
        j = min(len(B)-1, k - i)
        print 'i, j', i, j, A[i], B[j]

        if A[i] > B[j]:
            return self.findKth(A[:i], B[j:], i)
        else:
            return self.findKth(A[i:], B[:j], j)


class TestKth(unittest.TestCase):
    def _test_select_empty_array(self):
        A = [1, 3, 5, 7, 9]
        B = []
        a = Solution().findKth(A, B, 3)
        print a
        self.assertTrue(a == 7)

    def test_select_interleaved(self):
        A = [1, 3, 5, 7, 9, 11, 13]
        B = [2, 4, 6, 8, 10, 12, 14]
        a = Solution().findKth(A, B, 4)
        print a
        self.assertTrue(a == 5)

    def _test_one(self):
        A = [3]
        B = []
        a = Solution().findKth(A, B, 0)
        print a
        self.assertTrue(a == 3)

if __name__ == '__main__':
    unittest.main()
