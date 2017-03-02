class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        ret = 0
        first = 0
        while first < len(height) and height[first] == 0:
            first += 1
        last = len(height) - 1
        while last > -1 and height[last] == 0:
            last -= 1
        max = 0
        maxIndex = 0
        for i in range(len(height)):
            if height[i] > max:
                max = height[i]
                maxIndex = i
        j = 0
        while first <= maxIndex:
            if j == 0:
                j = height[first]
            elif height[first] < j:
                ret += j - height[first]
            else:
                j = height[first]
            first += 1
        j = 0
        while last >= maxIndex:
            if j == 0:
                j = height[last]
            elif height[last] < j:
                ret += j - height[last]
            else:
                j = height[last]
            last -= 1
        return ret
