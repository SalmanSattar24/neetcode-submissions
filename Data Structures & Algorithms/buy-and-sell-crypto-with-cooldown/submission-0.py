class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        memo = {}

        def recurse(i, holding):

            if i >= n:
                return 0
            
            key = (i, holding)
            if key in memo:
                return memo[key]
            
            if holding:

                sell = prices[i] + recurse(i + 2, not holding)
                skip = recurse(i + 1, holding)

                memo[key] = max(sell, skip)
            
            else:

                buy = -prices[i] + recurse(i + 1, not holding)
                skip = recurse(i + 1, holding)

                memo[key] = max(buy, skip)
            
            return memo[key]

        return recurse(0, False)