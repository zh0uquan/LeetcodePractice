class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # slow
        # return [n for n, val in Counter(nums) if val > len(num) / 2]

        # average
        d = collections.defaultdict(int)
        for i in nums:
            d[i] += 1
            if d[i] > len(nums) / 2:
                return i
