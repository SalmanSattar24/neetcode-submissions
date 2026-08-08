class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        L1, L2, L3 = len(s1), len(s2), len(s3)
        memo = {}

        def recurse(i, j, k):

            if k == L3:
                return i == L1 and j == L2
            

            key = (i, j, k)
            if key in memo:
                return memo[key]
            
            take_s1 = False
            if i < L1 and s1[i] == s3[k]:
                take_s1 = recurse(i + 1, j, k + 1)

            take_s2 = False
            if j < L2 and s2[j] == s3[k]:
                take_s2 = recurse(i, j + 1, k + 1)

            memo[key] = take_s1 or take_s2
            return memo[key]

        return recurse(0, 0, 0)