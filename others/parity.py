import unittest
import sys


def parity_of(input_int):
    # Kerningham way
    count = 0
    while input_int:
        input_int &= input_int - 1  # unset the least significant bit which is set.
        count += 1
    return count


def naive_parity(input_int):
    count = 0
    while input_int:
        count += input_int & 1  # count if last bit is set
        input_int >>= 1  # right shift a bit every time
    return count


class ParityByLookup(object):
    def __init__(self):
        self.bit_set_table_256 = [None] * 256
        self.bit_set_table_256[0] = 0
        for i in range(256):
            self.bit_set_table_256[i] = (i & 1) + self.bit_set_table_256[i / 2]

    def lookup(self, input_int):
        c = 0
        while input_int:
            c += self.bit_set_table_256[input_int & 0xff]
            input_int >>= 8
        return c


class TestParity(unittest.TestCase):
    def test_kerningham_parity(self):
        self.assertTrue(parity_of(0) == 0)
        self.assertTrue(parity_of(123) == 6)
        ans = parity_of(sys.maxsize)
        self.assertTrue(ans == 63, 'expected: 63 actual: %d' % ans)

    def test_naive_parity(self):
        self.assertTrue(naive_parity(0) == 0)
        self.assertTrue(naive_parity(123) == 6)

    def test_lookup_parity(self):
        sol = ParityByLookup()
        ans = sol.lookup(sys.maxsize)
        self.assertTrue(ans == 63, 'expected: 63 actual: %d' % ans)

if __name__ == '__main__':
    unittest.main()
