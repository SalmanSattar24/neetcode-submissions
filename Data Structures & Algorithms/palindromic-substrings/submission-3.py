class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        memo = {}

        for i in reversed(range(len(s))):
            for j in range(i, len(s)):

                if (
                    s[i] == s[j] and 
                    (j - i <= 2 or
                    memo.get((i + 1, j - 1), False))
                ):

                    memo[(i, j)] = True
                    res += 1

        return res