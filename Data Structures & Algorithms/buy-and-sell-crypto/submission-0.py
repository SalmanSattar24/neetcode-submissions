class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_day = 0
        max_profit = 0

        for today in range(len(prices)):

            if prices[today] < prices[buy_day]:
                buy_day = today
            
            elif prices[today] > prices[buy_day]:
                max_profit = max(max_profit, prices[today] - prices[buy_day])
        
        return max_profit