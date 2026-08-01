class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result, perm = [], []

        def backtrack():

            if len(perm) == len(nums):
                result.append(perm.copy())
            
            for num in nums:

                if num not in perm:

                    perm.append(num)
                    backtrack()

                    perm.pop()
        
        backtrack()
        return result