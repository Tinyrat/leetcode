class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = ''
        i = -1
        if len(strs) == 0:
            return ''
        while True:
            i += 1
            if len(strs[0]) > i:
                char = strs[0][i]
            else:
                break
            flag = 0
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != char:
                    flag = 1
                    break
            if flag == 1:
                break
            else:
                s += char
        return s


print Solution().longestCommonPrefix(['aa', 'a'])
