class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        L1, L2 = len(s), len(t)
        memo = defaultdict(int)

        def recurse(i, j):

            if j >= L2:
                return 1
            
            if i >= L1:
                return 0
            
            key = (i, j)
            if key in memo:
                return memo[key]
            
            memo[key] += recurse(i + 1, j)

            if s[i] == t[j]:
                memo[key] += recurse(i + 1, j + 1)

            return memo[key]
        
        return recurse(0, 0)