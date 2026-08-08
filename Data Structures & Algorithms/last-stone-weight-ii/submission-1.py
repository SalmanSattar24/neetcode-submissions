class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        target = sum(stones) // 2
        n = len(stones)
        total_sum = sum(stones)
        memo = {}
     
        for i in reversed(range(n + 1)):
            for s in reversed(range(total_sum + 1)):

                key = (i, s)
                if i >= n:
                    memo[key] = abs(s - (sum(stones) - s))
                    continue


                take = memo.get((i + 1, s + stones[i]), math.inf)
                skip = memo.get((i + 1, s), math.inf)

                memo[key] = min(take, skip)
        
        return memo[(0, 0)]
        