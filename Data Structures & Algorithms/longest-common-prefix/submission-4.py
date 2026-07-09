class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_len = len(min(strs))

        for i in range(min_len):
            for s in strs:

                if s[i] != strs[0][i]:
                    return s[:i]
        
        return min(strs)