class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        if 'MMM' in s:
            ret += 3000
        elif 'MM' in s:
            ret += 2000
        elif s[0] == 'M':
            ret += 1000
        if 'CM' in s:
            ret += 900
        elif 'DCCC' in s:
            ret += 800
        elif 'DCC' in s:
            ret += 700
        elif 'DC' in s:
            ret += 600
        elif 'CD' in s:
            ret += 400
        elif 'D' in s:
            ret += 500
        elif 'CCC' in s:
            ret += 300
        elif 'CC' in s:
            ret += 200
        elif 'C' in s and 'XC' not in s or 'CXC' in s:
            ret += 100
        if 'XC' in s:
            ret += 90
        elif 'LXXX' in s:
            ret += 80
        elif 'LXX' in s:
            ret += 70
        elif 'LX' in s:
            ret += 60
        elif 'XL' in s:
            ret += 40
        elif 'L' in s:
            ret += 50
        elif 'XXX' in s:
            ret += 30
        elif 'XX' in s:
            ret += 20
        elif 'X' in s and 'IX' not in s or 'XIX' in s:
            ret += 10
        if 'IX' in s:
            ret += 9
        elif 'VIII' in s:
            ret += 8
        elif 'VII' in s:
            ret += 7
        elif 'VI' in s:
            ret += 6
        elif 'IV' in s:
            ret += 4
        elif 'V' in s:
            ret += 5
        elif 'III' in s:
            ret += 3
        elif 'II' in s:
            ret += 2
        elif 'I' in s:
            ret += 1
        return ret
