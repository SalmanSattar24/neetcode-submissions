class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_map = [0] * 26

        len_s, len_t = len(s), len(t)

        if len_s != len_t:
            return False
        
        for i in range(len_s):

            char_s, char_t = s[i], t[i]

            freq_map[ord(char_s) - ord('a')] += 1
            freq_map[ord(char_t) - ord('a')] -= 1

        for val in freq_map:
            if val != 0:
                return False
        
        return True