class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # res = []
        # i = j = 0
        # nums1.sort()
        # nums2.sort()
        #
        # while i < len(nums1) and j < len(nums2):
        #     nums1Tmp, nums2Tmp = nums1[i], nums2[j]
        #     if nums1Tmp > nums2Tmp:
        #         j += 1
        #     elif nums1Tmp < nums2Tmp:
        #         i += 1
        #     else:
        #         if len(res) == 0 or res[-1] != nums1Tmp:
        #             res.append(nums1Tmp)
        #         i += 1
        #         j += 1
        #
        # return res

        return list(set(nums1) & set(nums2))
