class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        profit = 0

        for sell in prices:
            profit = max(profit, sell - minbuy)
            minbuy = min(minbuy, sell)
        
        return profit