import sys
class Justify(object):
    def __init__(self, text, maxWidth):
        self.words = text
        self.maxWidth = maxWidth

    def fullJustify(self):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        text_len = len(self.words)
        dp = [0]*text_len
        parent = [0]*text_len

        dp[-1] = self.badness([self.words[-1]])
        parent[-1] = text_len - 1

        for i in range(text_len-2, -1, -1):
            min_score = sys.maxint
            min_split = None
            for j in range(i+1, text_len):
                badness = dp[j] + self.badness(self.words[i:j])
                if badness < min_score:
                    min_score = badness
                    min_split = j
            dp[i] = min_score
            parent[i] = min_split

        print dp
        print parent

    def badness(self, text):
        word_len = sum([len(i) for i in text])
        sentence_len = word_len + len(text) - 1
        print 'badness:', text
        if sentence_len > self.maxWidth:
            print sys.maxint
            return sys.maxint
        else:
            print pow(self.maxWidth - sentence_len, 2)
            return pow(self.maxWidth - sentence_len, 2)

tool = Justify(["This", "is", "an", "example", "of", "text", "justification."], 25)
tool.fullJustify()
