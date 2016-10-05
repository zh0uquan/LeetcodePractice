class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([prices[i+1] - prices[i] for i in range(len(prices)-1) if prices[i+1] > prices[i]])

print(Solution().maxProfit([7,2,4,5,6,1,2]))
