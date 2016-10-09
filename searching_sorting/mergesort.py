import random

def mergesort(alist):
    _mergesort(alist, 0, len(alist)-1)

def _mergesort(alist, first, last):
    mid = (first+last)/2
    if first < last:
        _mergesort(alist, first, mid)
        _mergesort(alist, mid+1, last)

    i, j, k = first, mid+1, 0
    temp = [None]*(last-first+1)

    while i <= mid and j <= last:
        if alist[i] < alist[j]:
            temp[k] = alist[i]
            i += 1
        elif alist[i] >= alist[j]:
            temp[k] = alist[j]
            j += 1
        k += 1

    if i <= mid:
        temp[k:] = alist[i:mid+1]
    elif j <= last:
        temp[k:] = alist[j:last+1]

    alist[first:last+1] = temp
    # a = 0
    # print 'first: %d last:%d temp_len:%d' % (first, last, len(temp))
    # while first <= last:
    #     alist[first] = temp[a]
    #     first += 1
    #     a += 1

if __name__ == '__main__':
    l = random.sample(range(1, 100), 20)
    print l
    mergesort(l)
    print l