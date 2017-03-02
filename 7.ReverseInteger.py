import math


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        revx = int(str(abs(x))[::-1])
        if revx > math.pow(2, 31):
            return 0
        else:
            return revx * cmp(x, 0)
