class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        half = sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False
        
        n = len(nums)
        memo = {}

        def recurse(i, t):

            if t == half:
                return True
            
            if t > half or i >= n:
                return False
            
            key = (i, t)
            if key in memo:
                return memo[key]
            
            take = recurse(i + 1, t + nums[i])
            skip = recurse(i + 1, t)

            memo[key] = take or skip
            return memo[key]
        
        return recurse(0, 0)