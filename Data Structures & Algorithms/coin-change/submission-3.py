class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        N = len(coins)

# Top down DP
        # memo = {}

        # def recurse(remainder, denom):

        #     if denom >= N:
        #         return 1e9

        #     if remainder == 0:
        #         return 0
            
        #     key = (remainder, denom)
        #     if key in memo:
        #         return memo[key]
            
        #     min_coins = 1e9
            
        #     take = 1e9
        #     if remainder >= coins[denom]:
        #         take = 1 + recurse(remainder - coins[denom], denom)
            
        #     skip = 1e9
        #     skip = recurse(remainder, denom + 1)

        #     min_coins = min(take, skip)
                
        #     memo[key] = min_coins

        #     return memo[key]
        
        # result = recurse(amount, 0)

        # if result == 1e9:
        #     return -1
        
        # return result


# Bottom-Up DP
        
        # 1. Add the base case! It takes 0 coins to make amount 0.
        tab = {0: 0}
        
        for coin in coins:
            for remainder in range(1, amount + 1):
                
                take = 1e9
                if remainder >= coin:
                    # 2. Default uncalculated states to infinity
                    take = 1 + tab.get(remainder - coin, 1e9)
                
                # 3. Default the skip state to infinity
                skip = tab.get(remainder, 1e9)
                
                tab[remainder] = min(take, skip)
        
        # 4. Safely return -1 if the amount is unreachable
        ans = tab.get(amount, 1e9)
        return ans if ans != 1e9 else -1