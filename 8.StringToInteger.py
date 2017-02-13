import math


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = math.pow(2, 31) - 1
        MIN_INT = -math.pow(2, 31)
        sign = 1
        sum = 0
        flag = 0
        for char in str:
            if flag == 0:
                if char == ' ':
                    continue
                elif char == '+':
                    flag = 1
                    continue
                elif char == '-':
                    sign = -1
                    flag = 1
                    continue
                elif char >= '0' and char <= '9':
                    flag = 1
                    sum = sum * 10 + int(char)
                else:
                    break
            else:
                if char >= '0' and char <= '9':
                    sum = sum * 10 + int(char)
                else:
                    break
        sum *= sign
        if sum > MAX_INT:
            return int(MAX_INT)
        elif sum < MIN_INT:
            return int(MIN_INT)
        else:
            return sum


print Solution().myAtoi('-1 23')
