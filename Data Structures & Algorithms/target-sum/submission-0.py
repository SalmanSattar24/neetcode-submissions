class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo = {}

        def recurse(i, t):

            if i >= n:
                if t == target:
                    return 1
                else:
                    return 0
                
            
            key = (i, t)
            if key in memo:
                return memo[key]
            
            add = recurse(i + 1, t + nums[i])
            sub = recurse(i + 1, t - nums[i])

            memo[key] = add + sub
            return memo[key]
        
        return recurse(0, 0)