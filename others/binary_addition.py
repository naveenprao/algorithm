import array

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        maxlength = max(len(a), len(b))
        a = a.zfill(maxlength)
        b = b.zfill(maxlength)
        print maxlength, a, b
        sum = array.array('c')
        carry = 0
        idx = maxlength-1
        while idx >= 0:
            if a[idx] == b[idx] == '1':
                if carry == 1:
                    sum.dq_append('1')
                else:
                    sum.dq_append('0')
                    carry = 1

            elif a[idx] == b[idx] == '0':
                if carry == 1:
                    sum.dq_append('1')
                    carry = 0
                else:
                    sum.dq_append('0')

            elif a[idx] == '1' or b[idx] == '1':
                if carry == 1:
                    sum.dq_append('0')
                else:
                    sum.dq_append('1')
            idx -= 1

        if carry == 1:
            sum.dq_append('1')
        sum.reverse()
        return sum.tostring()

if __name__ == '__main__':
    sol = Solution()
    print sol.addBinary('11', '1')
