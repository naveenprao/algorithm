import math

class MaxHeap(object):
    def __init__(self, input_list):
        self.items = input_list
        # initialize lookup location for later random access.
        self.lookup = dict()
        for i in range(len(self.items)):
            self.lookup[self.items[i]] = i
        self.heap_size = len(input_list) - 1
        self.heap_max = len(input_list) - 1

    @classmethod
    def init_maxheap_of_size(cls, size=0):
        obj = cls([None]*size)
        obj.heap_size = 0
        obj.heap_max = size - 1
        return obj

    def swap(self, i, j):
        if i == j:
            return
        else:
            self.items[i], self.items[j] = self.items[j], self.items[i]
            # update lookup location of elements to new position.
            self.lookup[self.items[i]] = i
            self.lookup[self.items[j]] = j

    def heapify(self, i):
        if i > int(math.floor(len(self.items)/2)):
            return
        else:
            left = 2*i + 1
            right = 2*i + 2
            largest = i
            if left < len(self.items) and self.items[i] < self.items[left]:
                largest = left
            if right < len(self.items) and self.items[largest] < self.items[right]:
                largest = right

            if largest != i:
                self.swap(i, largest)
                self.heapify(largest)

    def build_heap(self):
        idx = int(math.floor(len(self.items)/2) - 1)
        while idx >= 0:
            self.heapify(idx)
            idx -= 1

    def insert(self, key):
        if self.heap_size == self.heap_max:
            raise ValueError("Heap overflow")

        self.items[self.heap_size + 1] = -1
        self.lookup[-1] = self.heap_size + 1
        self.increase_key(-1, key)

        self.heap_size += 1

    def increase_key(self, old_val, new_val):
        if old_val > new_val:
            return ValueError("New value cannot be smaller than older value.")
        pos = self.lookup[old_val]
        self.items[pos] = new_val

        def parent(idx):
            if idx % 2 == 0:
                return int((idx-1)/2)
            else:
                return int(idx/2)

        while pos > 0 and self.items[pos] > self.items[parent(pos)]:
            self.swap(pos, parent(pos))
            pos = parent(pos)

        del self.lookup[old_val]

    def maximum(self):
        if self.heap_size == 0:
            raise ValueError("Heap underflow !")

        return self.items[0]

    def extract_max(self):
        if self.heap_size == 0:
            raise ValueError("Heap underflow !")

        max_item = self.items[0]
        self.items[0] = self.items[self.heap_size]
        self.heap_size -= 1
        self.heapify(0)
        del self.lookup[max_item]
        return max_item

    def print_heap(self):
        print self.items[:self.heap_size + 1]
        print self.lookup

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    mh = MaxHeap(array)
    mh.build_heap()
    mh.print_heap()

    print mh.extract_max()
    print mh.maximum()
    mh.print_heap()

    mh.increase_key(1, 10)
    mh.print_heap()

    mh.insert(20)
    mh.print_heap()
