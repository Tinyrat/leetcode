class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tempS = ''
        for c in s:
            if c in '([{':
                tempS += c
            else:
                if c == ')':
                    cc = '('
                elif c == '}':
                    cc = '{'
                else:
                    cc = '['
                j = len(tempS) - 1
                if j < 0:
                    return False
                if tempS[j] == cc:
                    tempS = tempS[0:j]
                else:
                    return False
        if len(tempS) == 0:
            return True
        else:
            return False
