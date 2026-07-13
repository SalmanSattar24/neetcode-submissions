class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        
        def climb(step):

            if step == n:
                return 1
            
            if step > n:
                return 0
            
            if step in memo:
                return memo[step]

            memo[step] = climb(step + 1) + climb(step + 2)

            return memo[step]
        
        return climb(0)

