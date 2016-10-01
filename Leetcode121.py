class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        res, low = 0, prices[0]
        for i in prices:
            low = i if low < i else low
            res = i - low if i - low > res else res
        return res
