class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        n = len(piles)
        memo = {}

        def recurse(alice, i, m):

            if i >= n:
                return 0
            
            key = (alice, i, m)
            if key in memo:
                return memo[key]
            
            stones_taken = 0
            memo[key] = 0 if alice else math.inf

            for x in range(1, m * 2 + 1):

                if x + i > n:
                    break
                
                stones_taken += piles[x + i - 1]
                next_m = max(m, x)

                if alice:

                    memo[key] = max(
                        memo[key],
                        stones_taken + recurse(not alice, i + x, next_m)
                    )

                else:

                    memo[key] = min(
                        memo[key],
                        recurse(not alice, i + x, next_m)
                    )
                
            return memo[key]
        
        return recurse(True, 0, 1)