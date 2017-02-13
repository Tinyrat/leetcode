class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        next = [0, 0]
        j = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = next[j]
            if needle[i] == needle[j]:
                j += 1
            next.append(j)
        j = 0
        for i in range(0, len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - j + 1
        return -1


print Solution().strStr('', '')
