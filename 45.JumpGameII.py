class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        maxReach = 0
        nowReach = 0
        for i in range(len(nums)):
            if nowReach < i:
                ret += 1
                nowReach = maxReach
            maxReach = max(maxReach, i + nums[i])
        return ret

