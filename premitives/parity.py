import unittest

class Parity(object):

    def get_parity(self, i):
        bit_set = 0
        while i > 0:
            i &= i-1
            bit_set += 1

        return bit_set % 2

class TestParity(unittest.TestCase):
    def test_basic(self):
        p = Parity()
        self.assertTrue(p.get_parity(3) == 0)
        self.assertTrue(p.get_parity(2) == 1)

if __name__ == '__main__':
    unittest.main()
