class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_map_s = [0] * 26
        freq_map_t = [0] * 26

        len_s, len_t = len(s), len(t)

        if len_s != len_t:
            return False
        
        for i in range(len_s):

            char_s, char_t = s[i], t[i]

            freq_map_s[ord(char_s) - ord('a')] += 1
            freq_map_t[ord(char_t) - ord('a')] += 1

        return freq_map_s == freq_map_t