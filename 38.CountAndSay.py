class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = '1'
        count = 1
        while count < n:
            i = 0
            ret = ''
            while i < len(s):
                num = int(s[i])
                j = i
                while (j < len(s)) and (s[j] == s[i]):
                    j += 1
                ret = ret + str(j - i) + str(num)
                i = j
            count += 1
            s = ret
        return ret

