class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums) and nums[i] != val:
            i += 1
        j = i
        while j < len(nums):
            while j < len(nums) and nums[j] == val:
                j += 1
            if j < len(nums):
                nums[i] = nums[j]
                i += 1
                j += 1
        return i


print Solution().removeElement([3, 2, 2, 3], 3)
