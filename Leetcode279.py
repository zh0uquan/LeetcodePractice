import math
class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp = [float('inf')] * (n + 1)
        # dp[0] = 0
        # for i in range(1, n+1):
        #     if math.sqrt(i).is_integer():
        #         dp[i] = 1
        #         continue
        #     for n in range(i / 2, i+1):
        #         dp[i] = min(dp[i-n] + dp[n], dp[i])
        # return dp[n]

        dp = self._dp
        while len(dp) <= n:
            dp += [min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1]
        return dp[n]

if __name__ == '__main__':
    print(Solution().numSquares(28))
