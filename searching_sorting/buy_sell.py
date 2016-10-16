import unittest

class Solution(object):
    def maxProfit(self, arr):
        # If the array is empty, the maximum profit is zero.
        if len(arr) == 0:
            return 0

        # This recursive helper function implements the above recurrence.  It
        # returns a triple of (max profit, min array value, max array value).  For
        # efficiency reasons, we always reuse the array and specify the bounds as
        # [lhs, rhs]
        def Recursion(arr, lhs, rhs):
            # If the array has just one element, we return that the profit is zero
            # but the minimum and maximum values are just that array value.
            if lhs == rhs:
                return (0, arr[lhs], arr[rhs])

            # Recursively compute the values for the first and latter half of the
            # array.  To do this, we need to split the array in half.  The line
            # below accomplishes this in a way that, if ported to other languages,
            # cannot result in an integer overflow.
            mid = lhs + (rhs - lhs) / 2

            # Perform the recursion.
            ( leftProfit,  leftMin,  leftMax) = Recursion(arr, lhs, mid)
            (rightProfit, rightMin, rightMax) = Recursion(arr, mid + 1, rhs)

            # Our result is the maximum possible profit, the minimum of the two
            # minima we've found (since the minimum of these two values gives the
            # minimum of the overall array), and the maximum of the two maxima.
            maxProfit = max(leftProfit, rightProfit, rightMax - leftMin)
            return (maxProfit, min(leftMin, rightMin), max(leftMax, rightMax))

        # Using our recursive helper function, compute the resulting value.
        profit, _, _ = Recursion(arr, 0, len(arr) - 1)
        return profit

class Solution_test(unittest.TestCase):
    def test_monotonically_decreasing(self):
        cal = Solution()
        data = [10, 9, 8, 7, 6, 5, 4]
        sol = cal.maxProfit(data)
        self.assertTrue(sol == 0, (data, sol))

    def test_difference_not_the_answer(self):
        cal = Solution()
        data = [7, 1, 5, 3, 6, 4]
        sol = cal.maxProfit(data)
        self.assertTrue(sol == 5, (data, sol))

    def test_multiple_buy_sell(self):
        cal = Solution()
        data = [7, 1, 5, 3, 6, 4, 5, 11, 4, 5]
        sol = cal.maxProfit(data)
        self.assertTrue(sol == 4, (data, sol))

if __name__ == '__main__':
    unittest.main()
