class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return None
        ret = []
        wordLength = len(words[0])
        wordDic = {}
        for word in words:
            if wordDic.get(word) == None:
                wordDic[word] = 1
            else:
                wordDic[word] += 1
        for i in range(0, len(s) - len(words) * wordLength + 1):
            j = 0
            wordTemp = {}
            while j < len(words):
                str = s[i + j * wordLength:i + j * wordLength + wordLength]
                if str in words:
                    if str not in wordTemp:
                        wordTemp[str] = 1
                    else:
                        wordTemp[str] += 1
                    if wordTemp[str] > wordDic[str]:
                        break
                else:
                    break
                j += 1
            if j == len(words):
                ret.append(i)
        return ret

