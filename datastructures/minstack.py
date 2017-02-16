import unittest

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.datastack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # insert into min stack
        if len(self.datastack) == 0:
            self.minstack.append(x)
        elif x <= self.minstack[-1]:
            self.minstack.append(x)

        # insert into data stack
        self.datastack.append(x)
        self.display()

    def pop(self):
        """
        :rtype: void
        """
        # self.display()
        data = self.datastack.pop()
        if data == self.minstack[-1]:
            self.minstack.pop()
        return data

    def top(self):
        """
        :rtype: int
        """
        # print 'top', self.datastack[-1]
        return self.datastack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

    # def display(self):
    #     print 'data:', self.datastack
    #     print 'min:', self.minstack

class TestMinStack(unittest.TestCase):
    def test_min(self):
        ms = MinStack()
        ms.push(-3)
        ms.push(0)
        ms.push(-2)
        self.assertTrue(ms.getMin() == -3)
        self.assertTrue(ms.top() == -2)

    def test_min_after_pop(self):
        ms = MinStack()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        self.assertTrue(ms.pop() == -3)
        self.assertTrue(ms.getMin() == -2)
        self.assertTrue(ms.top() == 0)


if __name__ == '__main__':
    unittest.main()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()