class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ret = 0
        i = 0
        min = 100000000
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if abs(temp - target) < min:
                    min = abs(temp - target)
                    ret = temp
                if temp < target:
                    j += 1
                elif temp > target:
                    k -= 1
                else:
                    return target
            i += 1
        return ret
