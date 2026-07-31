class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        N = len(candidates)
        
        result = []
        subset = []

        def backtrack(i, s):

            if s == target:
                result.append(subset.copy())
                return

            if s > target or i >= N:
                return

            subset.append(candidates[i])
            backtrack(i + 1, s + candidates[i])

            subset.pop()

            while i + 1 < N and candidates[i] == candidates[i + 1]:
                i += 1

            backtrack(i + 1, s)
        

        backtrack(0, 0)
        return result