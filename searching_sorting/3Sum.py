import time

import time


class Solution(object):
    def threeSum(self, nums):
        lookup = dict()
        for num in nums:
            count = lookup.get(num, 0)
            lookup[num] = count + 1

        three_set_ans = set()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)-1):
                firstNum = nums[i]
                secondNum = nums[j]

                lookup[firstNum] += -1  # remove element from lookup
                lookup[secondNum] += -1  # add element back to lookup

                diff = -1*(firstNum+secondNum)
                if diff in lookup and lookup[diff] > 0:
                    three_set_ans.add(tuple(sorted((firstNum, secondNum, diff))))

                lookup[firstNum] += 1
                lookup[secondNum] += 1

        ans_list = list()
        for _tuple in three_set_ans:
            ans_list.append(list(_tuple))
        return ans_list



if __name__ == '__main__':
    start = time.time()
    test_nums = [11, 4, 9, -7, -7, 4, -6, 13, 12, -1, -5, -15, -2, -4, 7, 14, 14, 13, -2, -11, -9, -3, -15, 6, -4, 14, -7,
                 -15, 2, 2, 7, -10, 13, -6, -1, 14, 5, 8, 12, 3, 14, -15, 3, -10, -4, -12, -11, -4, -14, -6, -8, 14, 6, -15,
                 5, 10, 14, 13, 10, -6, -8, -6, -1, -9, 3, 13, -10, -6, -1, 9, 4, -2, 9, 14, 3, -9, -13, -1, -6, 10, 8, -7,
                 9, -8, -7, -1, 9, -15, -3, 4, -6, 5, 13, 8, 3, -6, -1, 8, -5, 13, 2, 14, -12, -11, 13, -1, -13, 8, 13, -4,
                 3, -1, -4, -2, -2, 5, 12, -8, 5, -13, 3, 14]

    # test_nums = [-1, 2, 0, -1, 4]
    driver = Solution()
    print driver.threeSum(test_nums)
    print time.time() - start