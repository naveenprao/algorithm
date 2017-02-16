# import unittest

class DutchPartition(object):
    def partition(self, arr, start, end, index):
        arr[index], arr[end] = arr[end], arr[index]
        i = start-1
        for j in range(start, end):
            print 'status - ', i, j
            if arr[j] <= arr[end]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                print 'swapped', arr
            print arr
        arr[i+1], arr[end] = arr[end], arr[i+1]
        print 'final', arr

        i = end + 1
        for j in range(end, -1, -1):
            print 'rev-', i, j
            if arr[j] >= arr[end]:
                i -= 1
                arr[i], arr[j] = arr[j], arr[i]
                print 'reversed', arr
        print 'reversed final', arr

    def dutchpartition(self, arr, start, end, index):
        mid = arr[index]
        i, j, n = 0, 0, end
        while j <= n:
            if arr[j] < mid:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
            elif arr[j] > mid:
                arr[j], arr[n] = arr[n], arr[j]
                n -= 1
            else:
                j += 1
        print arr

if __name__ == "__main__":
    # l = [0, 1, 2, 0, 2, 1, 1]
    # l = [2, 8, 7, 1, 4, 4, 4, 4]
    l = [ 2, 1, 4, 4, 8, 7, 4, 4]
    tool = DutchPartition()
    # tool.partition(l, 0, 7, 7)
    tool.dutchpartition(l, 0, 7, 7)
