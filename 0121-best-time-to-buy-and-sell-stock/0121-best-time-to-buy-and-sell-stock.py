class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = prices[0]
        for sell in prices:
            res = max(res, sell - minPrice)
            minPrice = min(minPrice, sell)
        return res