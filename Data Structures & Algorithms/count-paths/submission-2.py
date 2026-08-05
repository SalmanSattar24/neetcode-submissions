class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {(m - 1, n - 1) : 1}

        def recurse(r, c):

            if r == m - 1 and c == n - 1:
                return 1
            
            if r >= m or c >= n:
                return 0
            
            key = (r, c)
            if key in memo:
                return memo[key]
            
            right = recurse(r, c + 1)
            down = recurse(r + 1, c)

            memo[key] = right + down
            return memo[key]

        recurse(0, 0)
        return memo[(0, 0)]