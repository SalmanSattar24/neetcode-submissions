class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        N = len(nums)
        subsets = []

        def recurse(i, subset):

            if i == N:
                subsets.append(subset)
                return
            
            recurse(i + 1, subset + [nums[i]])
            recurse(i + 1, subset)

        recurse(0, [])

        return subsets