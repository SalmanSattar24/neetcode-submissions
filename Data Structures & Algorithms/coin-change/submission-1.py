class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        N = len(coins)

        memo = {}

        def recurse(remainder, denom):

            if denom >= N:
                return 1e9

            if remainder == 0:
                return 0
            
            key = (remainder, denom)
            if key in memo:
                return memo[key]
            
            min_coins = 1e9
            
            take = 1e9
            if remainder >= coins[denom]:
                take = 1 + recurse(remainder - coins[denom], denom)
            
            skip = recurse(remainder, denom + 1)

            min_coins = min(take, skip)
                
            memo[key] = min_coins

            return memo[key]
        
        result = recurse(amount, 0)

        if result == 1e9:
            return -1
        
        return result