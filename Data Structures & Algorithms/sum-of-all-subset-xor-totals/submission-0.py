class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        N = len(nums)
        memo = {}

        def backtrack(i, total):

            if i == N:
                return total
            
            if (i, total) in memo:
                return memo[(i, total)]
            
            take = backtrack(i + 1, total ^ nums[i])
            skip = backtrack(i + 1, total)

            memo[i] = take + skip

            return memo[i]
        
        return backtrack(0, 0)