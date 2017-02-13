class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            j = len(nums) - 2
            while j > -1 and nums[j] >= nums[j + 1]:
                j -= 1
            if j == -1:
                nums.sort()
            else:
                min = nums[j + 1]
                minIndex = j + 1
                for k in range(j + 2, len(nums)):
                    if nums[k] > nums[j] and nums[k] <= min:
                        min = nums[k]
                        minIndex = k
                temp = nums[j]
                nums[j] = nums[minIndex]
                nums[minIndex] = temp
                x = j + 1
                y = len(nums) - 1
                while x < y:
                    temp = nums[x]
                    nums[x] = nums[y]
                    nums[y] = temp
                    x += 1
                    y -= 1
        return nums


print Solution().nextPermutation([1,3,1,3,3])
