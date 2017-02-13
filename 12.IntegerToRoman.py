class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        qian = ['', 'M', 'MM', 'MMM']
        bai = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        shi = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        ge = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        s = qian[num / 1000]
        num = num % 1000
        s += bai[num / 100]
        num = num % 100
        s += shi[num / 10]
        num = num % 10
        s += ge[num]
        return s
