class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        if target < nums[0] or target > nums[len(nums) - 1]:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        begin = left
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                left = mid
                if target == nums[right]:
                    left = right
                else:
                    right -= 1
        end = left
        if nums[begin] == target:
            return [begin, end]
        else:
            return [-1, -1]

