class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Fixed: profit, not porfit
        max_porfit = 0 
        #first day is the default buy price
        min_price = prices[0]

        for price in prices:
            #if current price is the smallest take it
            if price < min_price:
                min_price = price

            #calculating profit : current price - min_price
            profit = price - min_price

            #if profit is the greatest we seen its the max profit
            if profit > max_porfit:
                max_porfit = profit
        
        return max_porfit
            

            
        