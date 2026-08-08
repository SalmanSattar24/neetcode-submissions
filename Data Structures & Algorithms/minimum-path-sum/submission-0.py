class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        R, C = len(grid), len(grid[0])
        memo = defaultdict(int)

        def recurse(r, c):

            key = (r, c)

            if (
                r >= R or r < 0 or
                c >= C or c < 0
            ):
                return math.inf

            if key == (R - 1, C - 1):
                return grid[R - 1][C - 1]
            
            if key in memo:
                return memo[key]
            
            right = grid[r][c] + recurse(r, c + 1)
            down = grid[r][c] + recurse(r + 1, c)

            memo[key] = min(right, down)
            return memo[key]

        return recurse(0, 0)