class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1, l2 = len(s), len(p)
        memo = {}

        def recurse(i, j):
            # Base case: if pattern is exhausted, string must be exhausted
            if j == l2:
                return i == l1
            
            key = (i, j)
            if key in memo:
                return memo[key]
            
            # Check if current characters match (and ensure i is in bounds!)
            match = i < l1 and (s[i] == p[j] or p[j] == '.')
            
            # If the next character is a '*'
            if j + 1 < l2 and p[j + 1] == '*':
                # We have two choices:
                # 1. Skip the '*' and the character before it (j + 2)
                # 2. Use the '*' if there is a match (i + 1), and keep the pattern at j
                memo[key] = recurse(i, j + 2) or (match and recurse(i + 1, j))
            else:
                # Normal match without a '*'
                memo[key] = match and recurse(i + 1, j + 1)
            
            return memo[key]
        
        return recurse(0, 0)