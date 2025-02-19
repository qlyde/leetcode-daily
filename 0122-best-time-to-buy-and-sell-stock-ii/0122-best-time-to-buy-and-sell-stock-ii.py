class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        res = 0
        for i in range(len(prices) - 1):
            res += max(0, prices[i + 1] - prices[i])
        return res

