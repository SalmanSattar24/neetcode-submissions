class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        R = len(triangle)
        memo = defaultdict(int)
      
        for r in reversed(range(R)):
            for c in reversed(range(len(triangle[r]))):

                key = (r, c)

                memo[key] = triangle[r][c] + (
                    min(
                        memo.get((r + 1, c), 0), 
                        memo.get((r + 1, c + 1), 0)
                    )
                )

        
        return memo[(0, 0)]