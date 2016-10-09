import time


class Solution(object):
    def _threeSum(self, nums, total):
        lookup = dict()
        for num in nums:
            count = lookup.get(num, 0)
            lookup[num] = count + 1

        print lookup

        def _twoSum(total):
            two_set_ans = set()
            for num in nums:
                if lookup[num] > 0:
                    remainder = total - num
                    lookup[num] += -1
                    if remainder in lookup and lookup[remainder] > 0:
                        tup = tuple(sorted((num, remainder)))
                        two_set_ans.add(tup)
                    lookup[num] += 1

            return list(two_set_ans)

        # return _twoSum(total)

        three_set_ans = set()
        for num in nums:
            lookup[num] += -1  # remove element from lookup
            pairs = _twoSum(total - num)
            lookup[num] += 1  # add element back to lookup

            for pair in pairs:
                new_list = list(pair)
                new_list.append(num)
                three_set_ans.add(tuple(sorted(new_list)))

        ans_list = list()
        for _tuple in three_set_ans:
            ans_list.append(list(_tuple))
        return ans_list

    def threeSum(self, nums):
        return self._threeSum(nums, 0)


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
