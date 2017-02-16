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
            if num[j] <= pivot:
                _swap(i+1, j)
                i += 1
            j += 1
            print num, i, j

        _swap(i, first)
        return i

    def _quicksort(first, last):
        if first < last:
            split = _partition(first, last)
            print num[:split], num[split:]
            _quicksort(first, split-1)
            _quicksort(split+1, last)

    _quicksort(0, len(num)-1)


if __name__ == "__main__":
    # num = random.sample(range(100), 10)
    # num = [-3, 0, -1, 1, 1, 2, 2, 4, 2]
    num = [2, 0, 1, 2, 0, 2, 1, 1]
    print num
    quicksort(num)
    print num
