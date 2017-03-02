class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zigzag = []
        for i in range(0, numRows):
            zigzag.append([])
        j = 0
        if numRows > 1:
            flag = 1
        else:
            flag = 0
        for i in range(0, len(s)):
            zigzag[j].append(s[i])
            j += flag
            if (j == numRows - 1) or (j == 0):
                flag *= -1
        s = ''
        for a in zigzag:
            for char in a:
                s += char
        return s

