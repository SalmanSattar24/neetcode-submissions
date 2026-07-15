class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        N = len(coins)

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


        
        tab = {0 : 0}

        for coin in coins:
            for remainder in range(1, amount + 1):
                
                take = 1e9
                if remainder >= coin:
                    take = 1 + tab.get(remainder - coin, 1e9)
                
                skip = 1e9
                skip = tab.get(remainder, 1e9)

                tab[remainder] = min(take, skip)
        
        ans = tab.get(amount, 1e9)
        return ans if ans != 1e9 else -1