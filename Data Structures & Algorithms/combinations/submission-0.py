class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        subset = []

        def backtrack(i, e):

            if e == k:
                result.append(subset.copy())
                return
            
            if e > k or i > n:
                return 
            
            subset.append(i)
            backtrack(i + 1, e + 1)

            subset.pop()
            backtrack(i + 1, e)
        

        backtrack(1, 0)
        return result