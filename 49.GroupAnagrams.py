class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = []
        standard = {}
        for str in strs:
            sortedStr = ''.join(sorted(str))
            if sortedStr in standard:
                standard[sortedStr].append(str)
            else:
                standard[sortedStr] = [str]
        for key in standard:
            ret.append(sorted(standard[key]))
        return ret
