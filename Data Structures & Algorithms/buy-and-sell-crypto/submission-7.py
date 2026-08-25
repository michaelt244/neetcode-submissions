class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxx = 0
        while(l < r):
            if(prices[r] > prices[l]):
                val = prices[r] - prices[l]
                if(val > maxx):
                    maxx = val
            l += 1 
            r -= 1
        return maxx