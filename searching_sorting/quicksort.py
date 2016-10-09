import random

def quicksort(num):

    def _swap(i, j):
        if i == j:
            return
        if num[i] == num[j]:
            return
        temp = num[i]
        num[i] = num[j]
        num[j] = temp

    def _partition(first, last):
        pivot = num[first]
        i, j = first, first+1
        while j <= last:
            if num[j] > pivot:
                j += 1
            elif num[j] <= pivot:
                _swap(i+1, j)
                i += 1
                j += 1

        _swap(i, first)
        return i

    def _quicksort(first, last):
        if first < last:
            split = _partition(first, last)
            _quicksort(first, split-1)
            _quicksort(split+1, last)

    _quicksort(0, len(num)-1)


if __name__ == "__main__":
    num = random.sample(range(100), 1)
    print num
    quicksort(num)
    print num
