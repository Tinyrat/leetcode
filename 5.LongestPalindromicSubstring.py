class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max = 1
        ret = s[0]
        for i in range(1, len(s)):
            count = 1
            j = 1
            while (i - j >= 0) and (i + j < len(s)) and s[i - j] == s[i + j]:
                j += 1
                count += 2
            if count > max:
                max = count
                ret = s[i - j + 1:i + j]
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                count = 0
                j = 0
                while (i - j >= 0) and (i + 1 + j < len(s)) and (s[i - j] == s[i + 1 + j]):
                    j += 1
                    count += 2
                if count > max:
                    max = count
                    ret = s[i - j + 1:i + 1 + j]
        return ret


print Solution().longestPalindrome('cbbd')
