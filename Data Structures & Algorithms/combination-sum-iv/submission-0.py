class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo =  defaultdict(int)

        def recurse(t):

            if t == target:
                return 1
            
            if t > target:
                return 0
            
            if t in memo:
                return memo[t]

            for num in nums:
                memo[t] += recurse(t + num)
            
            return memo[t]
        
        return recurse(0)
        return memo[(0)]