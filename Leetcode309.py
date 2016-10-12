class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy[i] = max(sell[i-2] - price, buy[i-1])
        # sell[i] = max(buy[i-1] + price, sell[i-1])
        #
        # https://discuss.leetcode.com/topic/30421/share-my-thinking-process/2
        if len(prices) < 2:
            return 0
        sell, buy, prevSell, prevBuy = 0, -prices[0], 0, 0
        for price in prices:
            prevBuy = buy
            buy = max(prevSell - price, prevBuy)
            prevSell = sell
            sell = max(prevBuy + price, prevSell)
        return sell
