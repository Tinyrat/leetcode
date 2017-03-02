class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        store = []
        i = 0
        j = 0
        while i < len(s):
            while (j < len(s)) and (s[j] not in store):
                store.append(s[j])
                j += 1
                if len(store) > ret:
                    ret = len(store)
            if (j < len(s)):
                while s[i] != s[j]:
                    store.remove(s[i])
                    i += 1
                store.remove(s[i])
                i += 1
            else:
                break
        return ret


