class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        for i in range(0, len(nums) - 3):
            for j in range(len(nums) - 1, i + 2, -1):
                if (i > 0 and nums[i] == nums[i - 1]) or (j < len(nums) - 1 and nums[j] == nums[j + 1]):
                    continue
                p = i + 1
                q = j - 1
                while p < q:
                    temp = nums[i] + nums[j] + nums[p] + nums[q]
                    if temp < target:
                        p += 1
                    elif temp > target:
                        q -= 1
                    else:
                        ret.append([nums[i], nums[p], nums[q], nums[j]])
                        p += 1
                        q -= 1
                        while nums[p] == nums[p - 1] and p < q:
                            p += 1
                        while nums[q] == nums[q + 1] and p < q:
                            q -= 1
        return ret
