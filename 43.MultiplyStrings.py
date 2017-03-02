class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        ret = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                ret[i + j] += int(num1[i]) * int(num2[j])
        for i in range(len(ret) - 1):
            ret[i + 1] = ret[i + 1] + ret[i] / 10
            ret[i] = ret[i] % 10
        last = len(ret) - 1
        while last > -1 and ret[last] == 0:
            last -= 1
        if last == -1:
            return '0'
        retString = ''
        for i in range(last, -1, -1):
            retString = retString + str(ret[i])
        return retString
