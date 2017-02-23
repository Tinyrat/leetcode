class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sIndex = 0
        pIndex = 0
        sTemp = 0
        starIndex = -1
        while sIndex < len(s):
            if pIndex < len(p) and (p[pIndex] == s[sIndex] or p[pIndex] == '?'):
                sIndex += 1
                pIndex += 1
                continue
            if pIndex < len(p) and p[pIndex] == '*':
                starIndex = pIndex
                pIndex += 1
                sTemp = sIndex
                continue
            if starIndex > -1:
                pIndex = starIndex + 1
                sTemp += 1
                sIndex = sTemp
                continue
            return False
        while pIndex < len(p) and p[pIndex] == '*':
            pIndex += 1
        if pIndex == len(p):
            return True
        return False


print Solution().isMatch('aa', '*')
