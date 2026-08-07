class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        R, C = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[R - 1][C - 1] == 1:
            return 0
            
        memo = defaultdict(int)
        memo[(R - 1, C - 1)] = 1

        for r in reversed(range(R)):
            for c in reversed(range(C)):
                
                key = (r, c)
 
                if (
                    obstacleGrid[r][c] == 1 or
                    key == (R - 1, C - 1)
                ):
                    continue

                down = memo.get((r + 1, c), 0)
                right = memo.get((r, c + 1), 0)

                memo[key] = down + right
            
        return memo[(0, 0)]

        