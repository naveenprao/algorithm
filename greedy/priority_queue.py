import itertools
import unittest
# min-heap implementation
import heapq

class PriorityQueue(object):
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.counter = itertools.count()
        self.REMOVED = '<removed-task>'

    def add_item(self, item, priority = 0):
        # add an item or update the priority of an existing item
        if item in self.entry_finder:
            self.remove_item(item)
        count = self.counter.next()
        entry = [priority, count, item]
        self.entry_finder[item] = entry
        heapq.heappush(self.pq, entry)

    def remove_item(self, item):
        # Mark an existing item as REMOVED. Raise KeyError if not found.
        entry = self.entry_finder.pop(item)
        entry[-1] = self.REMOVED

    def pop_item(self):
        # Remove and return the lowest priority item
        while self.pq:
            priority, count, item = heapq.heappop(self.pq)
            if item is not self.REMOVED:
                del self.entry_finder[item]
                return priority, item
        raise KeyError('pop from an empty priority queue')

    def peek_priority(self, item):
        entry = self.entry_finder[item]
        return entry[0]

class TestPriorityQueue(unittest.TestCase):
    def test_simple_insert(self):
        pq = PriorityQueue()
        pq.add_item('v', 5)
        pq.add_item('z', 3)
        self.assertTrue(pq.pop_item() == (3, 'z'))

    def test_simple_delete(self):
        pq = PriorityQueue()
        pq.add_item('v', 5)
        pq.add_item('z', 3)
        pq.remove_item('z')
        self.assertTrue(pq.pop_item() == (5, 'v'))

    def test_simple_increase_priority(self):
        pq = PriorityQueue()
        pq.add_item('v', 5)
        pq.add_item('z', 3)
        pq.add_item('v', 2)
        self.assertTrue(pq.pop_item() == (2, 'v'))

    def test_simple_decrease_priority(self):
        pq = PriorityQueue()
        pq.add_item('v', 5)
        pq.add_item('z', 3)
        pq.add_item('z', 6)
        self.assertTrue(pq.peek_priority('v') == 5)
        self.assertTrue(pq.pop_item() == (5, 'v'))

if __name__ == '__main__':
    unittest.main()
