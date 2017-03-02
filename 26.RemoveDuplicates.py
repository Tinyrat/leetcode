class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        i = 0
        while i < len(nums) - 1 and nums[i] < nums[i + 1]:
            i += 1
        j = i
        while j < len(nums):
            while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                j += 1
            if j < len(nums) - 1:
                i += 1
                j += 1
                nums[i] = nums[j]
            else:
                break
        return i + 1

