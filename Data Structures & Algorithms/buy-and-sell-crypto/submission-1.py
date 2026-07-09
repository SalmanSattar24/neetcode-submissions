from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit that can be achieved by buying and
        selling a stock. You are allowed to complete at most one transaction.

        This solution iterates through the prices to find the optimal buy and
        sell points to maximize profit.

        Time Complexity: O(N)
            - The code iterates through the `prices` array once.
            - Operations inside the loop (comparisons, subtractions, max) are O(1).
            Therefore, the overall time complexity is linear with respect to
            the number of days (N).

        Space Complexity: O(1)
            - Only a few constant extra variables (`buy_day`, `max_profit`, `today`)
              are used, regardless of the input array size.
            Therefore, the overall space complexity is constant.
        """

        # `buy_day` stores the index of the day when a stock is considered bought.
        # It initially points to the first day.
        buy_day = 0

        # `max_profit` stores the maximum profit found so far.
        # It is initialized to 0, as no profit has been made yet.
        max_profit = 0

        # Iterate through the prices array using 'today' as the current day's index.
        # This loop checks every possible 'sell' day.
        for today in range(len(prices)):
            # If the price on 'today' is less than the price on `buy_day`,
            # it means we found a new lower price to "buy" the stock.
            # So, update `buy_day` to 'today'.
            if prices[today] < prices[buy_day]:
                buy_day = today
            # If the price on 'today' is greater than the price on `buy_day`,
            # it means we can potentially make a profit by selling today.
            # Calculate the potential profit and update `max_profit` if it's higher.
            elif prices[today] > prices[buy_day]:
                max_profit = max(max_profit, prices[today] - prices[buy_day])

        # After iterating through all possible sell days, `max_profit` will
        # hold the highest profit achievable.
        return max_profit