import random

def find_index(num):
    if len(num) == 0:
        return -1

    def _find_index(first, last):
        if first <= last:
            mid = (first+last)/2
            if num[mid] == mid:
                return mid
            elif num[mid] < mid:
                return _find_index(mid+1, last)
            elif num[mid] > mid:
                return _find_index(first, mid-1)
        else:
            return -1

    index = _find_index(0, len(num)-1)
    return index

if __name__ == '__main__':
    #nums = random.sample(range(-10, 100), 50)
    # index[ 0   1   2   3  4  5  6  7  8  9  10]
    nums = [-8, -6, -2, -1, 5, 6, 7, 8, 9, 12, 13]
    print find_index(nums)
