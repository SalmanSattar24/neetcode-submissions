class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}

        def recurse(r, c):

            if (
                r >= R or r < 0 or
                c >= C or c < 0 or
                obstacleGrid[r][c] == 1
            ):
                return 0

            if (r, c) == (R - 1, C - 1):
                return 1

            
            key = (r, c)
            if key in memo:
                return memo[key]

            down = recurse(r + 1, c)
            right = recurse(r, c + 1)

            memo[key] = down + right
            return memo[key]
        
        return recurse(0, 0)