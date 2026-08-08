class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        memo = {}

        def recurse(i, a):

            if i >= n or a > amount:
                return 0
            
            if a == amount:
                return 1
            
            key = (i, a)
            if key in memo:
                return memo[key]
            
            take = recurse(i, a + coins[i])
            skip = recurse(i + 1, a)

            memo[key] = take + skip
            return memo[key]
        
        return recurse(0, 0)