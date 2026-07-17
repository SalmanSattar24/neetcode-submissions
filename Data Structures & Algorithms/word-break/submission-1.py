class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        L = len(s)
        memo = {}

        def recurse(index):

            if index >= L:
                return True
            
            if index in memo:
                return memo[index]

            for word in wordDict:

                if (
                    len(word) + index <= L and
                    s[index : len(word) + index] == word
                ):
                    if (recurse(index + len(word))):
                        memo[index] = True
                        return True

            memo[index] = False
            return memo[index]

        return recurse(0)