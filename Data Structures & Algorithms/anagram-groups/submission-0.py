class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)


        for string in strs:

            key = [0] * 26

            for char in string:

                location = (ord(char) - ord('a')) + 1

                key[location] += 1
            
            anagrams[tuple(key)].append(string)
        
        return list(anagrams.values())