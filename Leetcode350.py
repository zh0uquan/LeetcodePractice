class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a & b).elements())

        # nums1.sort()
        # nums2.sort()
        #
        # res = []
        # i = j = 0
        # while i  < len(nums1) and j < len(nums2):
        #     n1, n2 = nums1[i], nums2[j]
        #     if n1 < n2:
        #         i += 1
        #     elif n1 > n2:
        #         j += 1
        #     else:
        #         res.append(n1)
        #         i += 1
        #         j += 1
        #
        # return res
