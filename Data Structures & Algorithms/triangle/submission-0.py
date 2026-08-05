class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        R = len(triangle)
        memo = {}

        def recurse(r, c):

            if r == R:
                return 0
            
            key = (r, c)
            if key in memo:
                return memo[key]
            
            memo[key] = triangle[r][c] + min(recurse(r + 1, c), recurse(r + 1,  c + 1))

            return memo[key]
        
        recurse(0, 0)
        return memo[(0, 0)]