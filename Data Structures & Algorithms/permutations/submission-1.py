class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result, perm, visited = [], [], set()

        def backtrack():

            if len(perm) == len(nums):
                result.append(perm.copy())
            
            for num in nums:

                if num not in visited:

                    perm.append(num)
                    visited.add(num)
                    backtrack()

                    perm.pop()
                    visited.remove(num)
        
        backtrack()
        return result