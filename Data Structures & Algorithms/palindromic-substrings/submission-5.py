class Solution:
    def countSubstrings(self, s: str) -> int:
        
        L = len(s)
        res = 0
        memo = [[False] * L for _ in range(L)]

        for i in reversed(range(L)):
            for j in range(i, L):

                if (
                    s[i] == s[j] and 
                    (j - i <= 2 or
                    memo[i + 1][j - 1])
                ):

                    memo[i][j] = True
                    res += 1

        return res