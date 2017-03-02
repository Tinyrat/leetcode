class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        temp = ''
        for i in range(n):
            temp += '('
        for i in range(n):
            temp += ')'
        ret.append(temp)
        while True:
            j = len(temp) - 1
            while True:
                if j < len(temp) - 1:
                    j -= 1
                while temp[j] == ')':
                    j -= 1
                if j == 0:
                    return ret
                tempLeft = 0
                tempRight = 0
                for i in range(0, j):
                    if temp[i] == '(':
                        tempLeft += 1
                    else:
                        tempRight += 1
                tempStr = temp[0:j]
                if tempLeft > tempRight:
                    tempRight += 1
                    tempStr += ')'
                    while tempLeft < n:
                        tempStr += '('
                        tempLeft += 1
                    while tempRight < n:
                        tempStr += ')'
                        tempRight += 1
                    ret.append(tempStr)
                    temp = tempStr
                    break
