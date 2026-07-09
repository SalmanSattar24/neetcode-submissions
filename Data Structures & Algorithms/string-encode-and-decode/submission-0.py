class Solution:

    def encode(self, strs: List[str]) -> str:

        # ["neet","code","love","you"]
        # "4#neet4#code4#love3#you"

        res = []

        for string in strs:

            res.append(str(len(string)))
            res.append('#')
            res.append(string)
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:

        res = []

        i = 0
        j = 0

        while i < len(s):

            j = i

            while s[j] != '#':

                j += 1
            
            word_len = int(s[i:j])

            i = j + 1
            j = i + word_len

            res.append(s[i:j])
        
            i = j
        
        return res