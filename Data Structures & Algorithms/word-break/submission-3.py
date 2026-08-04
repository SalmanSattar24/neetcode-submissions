class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        L = len(s)
        word_dict = set(wordDict)
        memo = {}

        def recurse(i):

            if i >= L:
                return True
            
            if i in memo:
                return memo[i]
            
            for j in range(i, L):

                w = s[i : j + 1]

                if w in word_dict:
                    
                    if recurse(j + 1):
                        
                        memo[i] = True
                        return True

            memo[i] = False
            return memo[i]
        

        recurse(0)
        return memo[0]