class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merges two strings alternately, character by character.

        Args:
            word1 (str): The first input string.
            word2 (str): The second input string.

        Returns:
            str: A new string with characters merged alternately.

        Time Complexity:
            O(N) - We iterate through the longer of the two strings once, where N is the total length of both strings.

        Space Complexity:
            O(N) - We store the merged result in a list, which takes up space proportional to the combined length of both strings.
        """

        read = 0  # Pointer to track the current index in both strings
        LW1 = len(word1)  # Length of the first string
        LW2 = len(word2)  # Length of the second string
        res = []  # List to store the merged characters (using list for efficient appends)

        # Iterate while there are characters left in either string
        while read < LW1 or read < LW2:
            if read < LW1:  # If `read` is within bounds of `word1`, append its character
                res.append(word1[read])
            if read < LW2:  # If `read` is within bounds of `word2`, append its character
                res.append(word2[read])
            read += 1  # Move to the next index

        return ''.join(res)  # Convert list to string and return the merged result
