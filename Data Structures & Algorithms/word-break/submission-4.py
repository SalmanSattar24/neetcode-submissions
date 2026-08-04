class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        L = len(s)
        word_dict = set(wordDict)
        memo = {L : True}

        for i in reversed(range(L)):
            
            memo[i] = False
            
            for j in range(i, L):

                w = s[i : j + 1]

                if w in word_dict and memo.get(j + 1, False):
                    
                    memo[i] = True
                    break
                        
        

        return memo[0]