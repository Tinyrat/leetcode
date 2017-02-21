class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ret = [[] for i in range(target + 1)]
        for num in candidates:
            for i in range(target - 1, 0, -1):
                if ret[i] != [] and num + i <= target:
                    for case in ret[i]:
                        add = case + [num]
                        add.sort()
                        if add == [1, 1, 1, 5]:
                            print [num, i]
                            print ret
                        if add not in ret[num + i]:
                            ret[num + i].append(add)
            if num <= target and ([num] not in ret[num]):
                ret[num].append([num])
        return ret[target]


print Solution().combinationSum([10, 1, 2, 7, 6, 1, 5], 8)
