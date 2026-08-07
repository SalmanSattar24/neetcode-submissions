class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        # Increase the limit to safely handle up to 50,000 elements
        sys.setrecursionlimit(60000)
        
        n = len(stoneValue)
        memo = {}

        def recurse(alice, i):

            if i >= n:
                return 0
            
            key = (alice, i)
            if key in memo:
                return memo[key]
            
            stones_taken = 0
            memo[key] = -math.inf if alice else math.inf

            for x in range(1, 4):

                if x + i > n:
                    break
                
                stones_taken += stoneValue[x + i - 1]

                if alice:

                    memo[key] = max(
                        memo[key],
                        stones_taken + recurse(not alice, i + x)
                    )

                else:

                    memo[key] = min(
                        memo[key],
                        -stones_taken + recurse(not alice, i + x)
                    )
                
            return memo[key]
        
        relative_advantage = recurse(True, 0)


        if relative_advantage > 0:
            return 'Alice'
        elif relative_advantage < 0:
            return 'Bob'
        else:
            return 'Tie'