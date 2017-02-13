class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flag = 0
        counts = []
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    flag = 1
                    counts = [i, j]
                    break
            if flag == 1:
                break
        return counts

print Solution().twoSum([1,2,3],5)