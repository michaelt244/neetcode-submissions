class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = min(prices)
        right = max(prices)

        if(right - low < 0):
            return 0
        return right - low
        