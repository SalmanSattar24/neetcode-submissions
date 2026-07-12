class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = defaultdict(list)

        for s in strs:

            signature = [0] * 26

            for char in s:

                signature[ord(char) - ord('a')] += 1
            
            anagram_map[tuple(signature)].append(s)

        
        result = []
        for _, val in anagram_map.items():

            result.append(val)
        
        return result