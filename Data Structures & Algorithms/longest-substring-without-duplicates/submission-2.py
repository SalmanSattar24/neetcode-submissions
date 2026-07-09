from typing import List # Though not explicitly used for the type hints, good practice to include if from typing import is present

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        This solution uses a sliding window approach with a hash set to efficiently
        track characters within the current window.

        Time Complexity: O(N)
            - Both the `left` and `right` pointers traverse the string at most once.
            - Set operations (add, remove, in) take O(1) on average.
            Therefore, the overall time complexity is linear with respect to
            the length of the string (N).

        Space Complexity: O(M)
            - `char_set` stores unique characters within the current window.
            - M is the number of unique characters in the input string, which can be
              at most 128 for ASCII characters or 26 for lowercase English letters.
            Therefore, the space complexity is proportional to the size of the
            character set.
        """

        # `char_set` will store the unique characters within the current sliding window.
        # This allows for O(1) average time complexity for checking membership.
        char_set = set()

        # `left` pointer defines the start of the current sliding window.
        left = 0

        # `max_len` stores the maximum length of a substring without duplicates found so far.
        # Initialized to 0, as no valid substring has been processed yet.
        max_len = 0

        # The `right` pointer iterates through the string, expanding the window.
        for right in range(len(s)):
            # If the character at the `right` pointer is already in `char_set`,
            # it means we have a duplicate within our current window.
            if s[right] in char_set:
                # While the duplicate character `s[right]` is still in the set,
                # we need to shrink the window from the left.
                while s[right] in char_set:
                    # Remove the character at the `left` pointer from the set.
                    char_set.remove(s[left])
                    # Move the `left` pointer one step to the right, shrinking the window.
                    left += 1

            # After the `if` block (and `while` loop if a duplicate was found),
            # the current character `s[right]` is guaranteed to be unique within the new window.
            # Add `s[right]` to the set to include it in the current window.
            char_set.add(s[right])

            # Update `max_len` if the current window's length is greater.
            # The length of the current window is calculated as `right - left + 1`.
            max_len = max(max_len, right - left + 1)

        # After iterating through the entire string, `max_len` will hold the
        # length of the longest substring without repeating characters.
        return max_len