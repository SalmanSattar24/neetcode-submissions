class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        R = len(triangle)
        memo = defaultdict(int)
        # for c in range(len(triangle[R - 1])):
        #     memo[(R, c)] = 0


            
        for r in reversed(range(R)):
            for c in reversed(range(len(triangle[r]))):

                key = (r, c)
                memo[key] = triangle[r][c] + (
                    min(memo.get((r + 1, c), 0), memo.get((r + 1, c + 1), 0))
                )

        
        return memo[(0, 0)]