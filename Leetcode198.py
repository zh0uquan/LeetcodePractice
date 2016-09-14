class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {-1: 0, -2: 0}
        for _, n in enumerate(nums):
            dp[_] = max(dp[_-2] + n, dp[_-1])
        return dp[len(nums)-1]


print(Solution().rob([1,2,34]))
