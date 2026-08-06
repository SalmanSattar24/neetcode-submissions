class Solution:
    def integerBreak(self, n: int) -> int:
        
        memo = defaultdict(int)
        memo[1] = 1
        
        for num in range(2, n + 1):
            for i in range(1, num):

                memo[num] = max(
                    memo[num],
                    i * (num - i), 
                    i * memo[num - i]
                )

        return memo[n]