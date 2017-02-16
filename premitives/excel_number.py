import unittest
class Excel(object):
    def decode_col_id(self, str):
        num = 0
        base = 26
        for i in range(len(str)):
            ascii = ord(str[i])
            if ascii < ord('A') or ascii > ord('Z'):
                return -1
            offset = ascii - ord('A') + 1
            num = num * base + offset

        return num

class TestExcel(unittest.TestCase):
    def test_single_letters(self):
        ex = Excel()
        print ex.decode_col_id("ZZ")

    def test_multi_letters(self):
        pass


if __name__ == "__main__":
    unittest.main()
