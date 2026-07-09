class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

        LW1 = len(word1)
        LW2 = len(word2)
        res = []
        read = 0

        while read < LW1 or read < LW2:

            if read < LW1:

                res.append(word1[read])
            
            if read < LW2:

                res.append(word2[read])
            
            read += 1
        

        return ''.join(res)