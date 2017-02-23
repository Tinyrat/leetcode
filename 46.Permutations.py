import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = sorted(nums)
        ret = [copy.deepcopy(temp)]
        while True:
            k = len(temp) - 1
            while k > 0 and temp[k - 1] >= temp[k]:
                k -= 1
            if k == 0:
                break
            k -= 1
            j = len(temp) - 1
            while temp[j] <= temp[k]:
                j -= 1
            tempNum = temp[k]
            temp[k] = temp[j]
            temp[j] = tempNum
            temp = temp[:k + 1] + sorted(temp[k + 1:])
            ret.append(copy.deepcopy(temp))
        return ret


print Solution().permute([1, 1, 3])
