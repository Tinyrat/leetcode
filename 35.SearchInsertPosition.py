class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        if target == nums[left]:
            return left
        elif target > nums[left]:
            return left + 1
        else:
            return left


print Solution().searchInsert([1, 3, 5, 6], 0)
