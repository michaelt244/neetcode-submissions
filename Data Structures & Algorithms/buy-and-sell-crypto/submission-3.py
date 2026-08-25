class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices) - 1
        max = 0
        while(l < r):
            if(prices[r] > prices[l]):
                val = prices[r] - prices[l]
                if(val > max):
                    max = val
                    r -= 1
            l += 1 