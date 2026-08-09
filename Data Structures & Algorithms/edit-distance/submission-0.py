class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        l1, l2 = len(word1), len(word2)
        memo = defaultdict(int)

        def recurse(i, j):

            if i >= l1:
                return l2 - j
            
            if j >= l2:
                return l1 - i
            
            key = (i, j)
            if key in memo:
                return memo[key]
            
            if word1[i] == word2[j]:
                memo[key] += 0 + recurse(i + 1, j + 1)

            else:

                memo[key] = min(
                    1 + recurse(i, j + 1),
                    1 + recurse(i + 1, j),
                    1 + recurse(i + 1, j + 1)
                )
            
            return memo[key]
        

        return recurse(0, 0)