class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_porfit = 0 
        min_price = prices[0]


        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price
            if profit > max_porfit:
                max_porfit = profit
        
        return max_porfit
            

            
        