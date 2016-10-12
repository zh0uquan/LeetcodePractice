class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return sum(nums)
        def rob(nums):
            prev = now = 0
            for n in nums:
                now, prev = max(prev + n, now)
            return now
        return max(rob(nums[1:]), rob(nums[:-1]))

if __name__ == '__main__':
    main()