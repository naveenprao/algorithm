import unittest

class StringToInt(object):
    def string_to_int(self, string):
        num = 0
        for i in xrange(len(string)):
            num = num * 10 + (ord(string[i]) - ord('0'))
        return num

    def int_to_string(self, i):
        str_array=[]
        while i > 0:
            j = i % 10
            str_array.append(str(j))
            i = i/10
        str_array.reverse()
        return ''.join(str_array)

class StringTest(unittest.TestCase):
    def test_string_to_int(self):
        util = StringToInt()
        i = util.string_to_int("123")
        print i
        self.assertTrue(i == 123)

    def test_int_to_str(self):
        util = StringToInt()
        i = util.int_to_string(124)
        print i
        self.assertTrue(i == "124")

if __name__ == '__main__':
    unittest.main()
