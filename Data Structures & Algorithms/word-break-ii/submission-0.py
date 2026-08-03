class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        results = []
        words = []

        def backtrack(i):

            if i == len(s):
                results.append(' '.join(words))
                return
            
            for j in range(i, len(s)):

                if (
                    s[i : j + 1] in wordDict
                ):

                    words.append(s[i : j + 1])
                    backtrack(j + 1)

                    words.pop()

        backtrack(0)
        return results