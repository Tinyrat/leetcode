class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            if target < nums[left] or target > nums[right]:
                return -1
            else:
                while left < right:
                    mid = (left + right) / 2
                    if target <= nums[mid]:
                        right = mid
                    else:
                        left = mid + 1
                if target == nums[left]:
                    return left
                else:
                    return -1
        else:
            while left < right:
                mid = (left + right) / 2
                if nums[mid] < nums[0]:
                    right = mid
                else:
                    left = mid + 1
            if target < nums[left] or target > nums[left - 1]:
                return -1
            elif target >= nums[0]:
                left = 0
                right = right - 1
            else:
                left = right
                right = len(nums) - 1
            while left < right:
                mid = (left + right) / 2
                if target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            if nums[left] == target:
                return left
            else:
                return -1


print Solution().search([4,5,6,7,0,1,2], 4)
