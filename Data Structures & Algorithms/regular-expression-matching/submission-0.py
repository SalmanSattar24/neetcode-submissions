class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        l1, l2 = len(s), len(p)
        memo = {}

        def recurse(i, j):

            if j >= l2:
                return i >= l1
            
            key = (i, j)
            if key in memo:
                return memo[key]


            match = i < l1 and (p[j] == s[i] or p[j] == '.')

            if j + 1 < l2 and p[j + 1] == '*':
                
                memo[key] = (

                    (match and recurse(i + 1, j)) or
                    recurse(i, j + 2)
                    
                )

            else:

                memo[key] = match and recurse(i + 1, j + 1)


            return memo.get(key, False)
        

        return recurse(0, 0)