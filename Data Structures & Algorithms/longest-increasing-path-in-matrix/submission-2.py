class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        sys.setrecursionlimit(20000)

        R, C = len(matrix), len(matrix[0])
        memo = {}

        def recurse(r, c, prev_val):

            if (
                min(r, c) < 0 or 
                r >= R or c >= C or
                matrix[r][c] <= prev_val
            ):
                return 0
            
            key = (r, c)
            if key in memo:
                return memo[key]
            
            right = 1 + recurse(r, c + 1, matrix[r][c])
            left = 1 + recurse(r, c - 1, matrix[r][c])
            up = 1 + recurse(r - 1, c, matrix[r][c])
            down = 1 + recurse(r + 1, c, matrix[r][c])

            memo[key] = max(right, left, up, down)
            return memo[key]

        LIS = 1
        for r in range(R):
            for c in range(C):

                LIS = max(LIS, recurse(r, c, -1))

        return max(memo.values())