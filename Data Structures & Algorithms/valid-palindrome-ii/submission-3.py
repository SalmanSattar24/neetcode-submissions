class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Determines if a given string can be a palindrome by removing at most one character.

        Args:
            s (str): The input string.

        Returns:
            bool: True if the string can be a palindrome with at most one deletion, False otherwise.
        """

        def is_palindrome(left: int, right: int) -> bool:
            """
            Helper function to check if a substring of `s` is a palindrome.

            Args:
                left (int): Left index of the substring.
                right (int): Right index of the substring.

            Returns:
                bool: True if the substring is a palindrome, False otherwise.
            """
            while left < right:
                if s[left] != s[right]:  # If mismatch found, it's not a palindrome
                    return False
                left += 1  # Move left pointer forward
                right -= 1  # Move right pointer backward
            return True  # If loop completes, it's a palindrome

        left, right = 0, len(s) - 1  # Initialize pointers at both ends of the string

        while left < right:
            if s[left] != s[right]:  # If mismatch found, try removing one character
                # Check if skipping either left or right index results in a palindrome
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1  # Move left pointer forward
            right -= 1  # Move right pointer backward

        return True  # If no mismatches found, the string is already a palindrome
