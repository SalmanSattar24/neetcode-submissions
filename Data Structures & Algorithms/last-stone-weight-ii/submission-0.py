class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        target = sum(stones) // 2
        n = len(stones)

        memo = {}

        def recurse(i, s):

            if i >= n:
                return abs(s - (sum(stones) - s))
            
            key = (i, s)
            if key in memo:
                return memo[key]
            
            take = recurse(i + 1, s + stones[i])
            skip = recurse(i + 1, s)

            memo[key] = min(take, skip)
            return memo[key]
        
        return recurse(0, 0)