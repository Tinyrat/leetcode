class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numToLetter = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ret = []
        if len(digits) == 0:
            return []
        count = [0 for i in range(0, len(digits))]
        while True:
            s = ''
            for i in range(len(digits)):
                s += numToLetter[int(digits[i])][count[i]]
            ret.append(s)
            j = len(digits) - 1
            while (j > -1) and (count[j] == len(numToLetter[int(digits[j])]) - 1):
                j -= 1
            if j == -1:
                break
            count[j] += 1
            for k in range(j + 1, len(digits)):
                count[k] = 0
        return ret

