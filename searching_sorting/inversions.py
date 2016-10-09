import random

def inversion(alist):
    inversions = [0]

    def _inversion(first, last):
        mid = (first + last) / 2
        if first < last:
            _inversion(first, mid)
            _inversion(mid+1, last)

        i, j, k = first, mid+1, 0
        temp = [None] * (last-first+1)
        while i <= mid and j <= last:
            if alist[i] < alist[j]:
                temp[k] = alist[i]
                i += 1
            elif alist[j] <= alist[i]:
                if alist[j] != alist[i]:
                    # inversion found
                    inversions[0] += (mid - i + 1)
                temp[k] = alist[j]
                j += 1
            k += 1

        if i > mid:
            temp[k:] = alist[j:last+1]
        else:
            temp[k:] = alist[i:mid+1]

        alist[first:last+1] = temp

    _inversion(0, len(alist)-1)
    return inversions[0]

if __name__ == '__main__':
    with open('/Personal/Coursera/Algo Stanford 1/Programming Assignment/data.txt') as input:
        content = input.readlines()
        num = []
        for line in content:
            num.append(int(line))

        print len(num)
        #l = random.sample(range(0, 100), 5)

    inv = inversion(num)
    print inv
