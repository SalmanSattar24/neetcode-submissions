class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: If the list contains only one string, return it as the prefix
        if len(strs) == 1:
            return strs[0]

        # Initialize an empty list to store the common prefix characters
        res = []

        # Iterate over the characters of the first string in the list
        for i in range(len(strs[0])):
            # Extract the current character from the first string
            char = strs[0][i]

            # Compare this character with the corresponding character in all other strings
            for string in strs:
                # If the current index exceeds the length of any string OR
                # the character at this index does not match across all strings, stop
                if i == len(string) or string[i] != char:
                    # Convert the list of characters into a string and return as the prefix
                    return ''.join(res)

            # If the character matches across all strings, add it to the result list
            res.append(char)

        # Convert the list of characters into a string and return as the final prefix
        return ''.join(res)
