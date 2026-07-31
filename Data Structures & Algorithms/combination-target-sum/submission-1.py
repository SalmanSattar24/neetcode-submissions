class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        N = len(nums)
        result = []
        
        def recurse(i, s, subset):

            if s == target:
                result.append(subset.copy())
                return
            
            if i >= N or s > target:
                return 
            
            recurse(i, s + nums[i], subset + [nums[i]])
            recurse(i + 1, s, subset)
        

        recurse(0, 0, [])
        return result