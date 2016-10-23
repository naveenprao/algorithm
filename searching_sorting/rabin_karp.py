import unittest
import logging
logging.basicConfig(level=logging.INFO)

class RabinKarp(object):
    def match(self, text, pattern, rad, prime):
        if len(pattern) > len(text):
            return None
        p_hash = 0
        t_hash = 0
        shift = (rad ^ (len(pattern) - 1))
        for i in range(len(pattern)):
            logging.debug('pattern: %d, %d, %d', ord(pattern[i]), rad*p_hash + ord(pattern[i]), p_hash)
            logging.debug('text: %d, %d, %d', ord(text[i]), rad * t_hash + ord(text[i]), t_hash)
            p_hash = (rad * p_hash + ord(pattern[i])) % prime
            t_hash = (rad * t_hash + ord(text[i])) % prime
        logging.debug('final: %d, %d', p_hash, t_hash)

        for s in range(len(text) - len(pattern) + 1):
            if p_hash == t_hash:
                if pattern == text[s:s + len(pattern)]:
                    logging.debug('pattern found at : %d', s)
                    return s
            if s < len(text) - len(pattern):
                t_hash = rad * (t_hash - ord(text[s + 1]) * shift) + ord(text[s + len(pattern)])
                t_hash %= prime


class TestRabinKarp(unittest.TestCase):
    def test_simple_match(self):
        text = "bacbababacacbab"
        pattern = "abac"
        self.assertTrue(RabinKarp().match(text, pattern, 26, 13) == 6)


if __name__ == '__main__':
    unittest.main()
