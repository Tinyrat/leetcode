class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        appear = [False for i in range(len(nums) + 1)]
        for num in nums:
            if num <= len(nums) and num > 0:
                appear[num] = True
        for i in range(1, len(appear)):
            if not appear[i]:
                return i
        return len(appear)

