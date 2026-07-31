class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        N = len(nums)
        result = []
        subset = []

        def backtrack(i, s):

            if s == target:
                result.append(subset.copy())
                return
            
            if i == N or s > target:
                return

            subset.append(nums[i])
            backtrack(i, s + nums[i])
            subset.pop()

            backtrack(i + 1, s)
    

        backtrack(0, 0)
        return result