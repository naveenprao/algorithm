import unittest


class KMP(object):
    def prefix_function(self, pattern):
        l = len(pattern)
        prefix = [0] * l
        match = 0
        for i in range(1, l):
            while match > 0 and pattern[match] != pattern[i]:
                match = prefix[match]
            if pattern[min(match, i - 1)] == pattern[i]:
                match += 1
            prefix[i] = match
        return prefix

    def matcher(self, text, pattern):
        prefix_fun = self.prefix_function(pattern)
        print prefix_fun
        q = 0
        for i in range(len(text)):
            while q > 0 and pattern[q] != text[i]:
                q = prefix_fun[q-1]
            if pattern[q] == text[i]:
                print 'match:', pattern[q:], text[i:], q
                q += 1
            if q == len(pattern):
                print "Found pattern at:", i - len(pattern) + 1, q
                yield i-len(pattern)+1
                q = prefix_fun[q-1]

        yield

class Test_Prefix(unittest.TestCase):
    def test_simple_prefix(self):
        string = 'ababaca'
        prefix = KMP().prefix_function(string)
        self.assertTrue(prefix == [0, 0, 1, 2, 3, 0, 1])


class Test_Search(unittest.TestCase):
    def test_simple_search(self):
        match = KMP().matcher("bacbababacacbab", "ababaca")
        self.assertTrue(match.next() == 4)
        self.assertTrue(match.next() is None)

if __name__ == '__main__':
    unittest.main()
