def find_one(nums):
    start = 0
    end = len(nums)-1
    print nums, start, end
    while start <= end:
        mid = start+(end-start)/2
        if nums[mid] == 1:
            return mid
        else:
            return max(find_one(nums[:mid]), mid+1+find_one(nums[mid+1:]))
    return -99999

def find_first(nums, k):
    start = 0
    end = len(nums)-1
    index = len(nums)
    while start <= end:
        mid = start+(end-start)/2
        print start, end, mid
        if nums[mid] == k and mid < index:
            index = mid
            end = mid-1
        elif nums[mid] > k:
            end = mid-1
        elif nums[mid] < k:
            start = mid + 1

    if index == len(nums):
        return -1
    else:
        return index

# print find_one([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0])
print find_first([-14, -10, 2, 108, 108, 285, 285, 285, 285, 401], 285)