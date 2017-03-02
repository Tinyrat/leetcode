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
            if num <= target:
                ret[num] = [[num]]
        for num in candidates:
            for i in range(target):
                if len(ret[i]) > 0 and num + i <= target:
                    for case in ret[i]:
                        add = case + [num]
                        add.sort()
                        if add not in ret[num+i]:
                            ret[num + i].append(add)
        return ret[target]
