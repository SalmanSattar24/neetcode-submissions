class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {(m - 1, n - 1) : 1}


        for r in reversed(range(m)):
            for c in reversed(range(n)):
                
                if r == m - 1 and c == n - 1:
                    continue
                    
                right = memo.get((r, c + 1), 0)
                down = memo.get((r + 1, c), 0)

                key = (r, c)
                memo[key] = right + down


        return memo[(0, 0)]