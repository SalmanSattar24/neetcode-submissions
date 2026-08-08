class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        L1, L2 = len(text1), len(text2)
        memo = {}

        def recurse(i, j):

            if i >= L1 or j >= L2:
                return 0

            key = (i, j)
            if key in memo:
                return memo[key]
            
            match = 0
            if text1[i] == text2[j]:
                match = 1 + recurse(i + 1, j + 1)

            alt_one = recurse(i + 1, j)
            alt_two = recurse(i, j + 1)

            memo[key] = max(match, alt_one, alt_two)
            return memo[key]
        
        return recurse(0, 0)