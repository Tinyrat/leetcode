class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = len(nums1) + len(nums2)
        nums3 = []
        count = 0
        i = 0
        j = 0
        while count < nums / 2 + 1:
            if (i == len(nums1)):
                nums3.append(nums2[j])
                j += 1
                count += 1
            elif (j == len(nums2)):
                nums3.append(nums1[i])
                i += 1
                count += 1
            else:
                if (nums1[i] <= nums2[j]):
                    nums3.append(nums1[i])
                    i += 1
                    count += 1
                else:
                    nums3.append(nums2[j])
                    j += 1
                    count += 1
        if (nums % 2 == 0):
            return (nums3[len(nums3) - 1] + nums3[len(nums3) - 2]) / 2.0
        else:
            return nums3[len(nums3) - 1]


print Solution().findMedianSortedArrays([], [1])
