from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time Complexity: O(L1 + L2)
        L1 = len(s1)
        L2 = len(s2)

        - Initializing s1_counter: O(L1) to iterate through s1.
        - The main loop iterates `right` from 0 to L2-1: O(L2) iterations.
        - Inside the loop:
          - Adding/removing characters from window_counter: O(1) on average.
          - The `while` loop (for shrinking): `left` pointer moves at most L2 times
            across the entire execution. Each character from s2 is added and removed
            from the window_counter at most once.
          - Comparing `s1_counter == window_counter`: O(1) for a fixed alphabet size
            (e.g., 26 for lowercase English letters).

        Space Complexity: O(1)
        - s1_counter: Stores at most 26 unique character frequencies.
        - window_counter: Stores at most 26 unique character frequencies.
        The space used is constant relative to the alphabet size, not the input string lengths.
        """

        # Edge case: If s1 is longer than s2, it's impossible for s2 to contain
        # a permutation of s1, so we can immediately return False.
        if len(s1) > len(s2):
            return False

        # --- Initialize Frequency Counters ---

        # s1_counter: Stores the required frequency of each character in s1.
        # This will be our target frequency map.
        # Example: s1 = "abc" -> s1_counter = {'a': 1, 'b': 1, 'c': 1}
        # Using Counter is efficient for building initial frequency maps.
        s1_counter = Counter(s1)

        # window_counter: Stores the frequency of characters in the current
        # sliding window within s2. We use defaultdict(int) so that when
        # we try to access a character that hasn't been seen yet, it defaults
        # to a count of 0, preventing KeyError.
        window_counter = defaultdict(int)

        # Initialize the left pointer of our sliding window.
        # This pointer will define the start of our current window.
        left = 0

        # --- Sliding Window Iteration ---

        # The 'right' pointer iterates through s2, expanding the window one character at a time.
        for right in range(len(s2)):
            # Get the character at the current 'right' pointer position.
            char_right = s2[right]

            # Add this character to our window's frequency counter.
            window_counter[char_right] += 1

            # --- Maintain Fixed Window Size ---

            # This `while` loop ensures that our sliding window (defined by `left` and `right`)
            # always has a size equal to `len(s1)`.
            # If the current window becomes larger than `len(s1)`, it means we've added
            # a new character at `right` and now need to remove one from `left` to keep
            # the window size constant.
            while (right - left + 1) > len(s1):
                # Get the character that is at the 'left' end of the window.
                char_left = s2[left]

                # Decrement its count in the window's frequency counter,
                # as it is no longer part of the window.
                window_counter[char_left] -= 1

                # Optimization: If a character's count drops to 0, it means
                # it's no longer present in the window. We can remove it
                # from the `window_counter` dictionary to keep it clean
                # and ensure accurate comparison with `s1_counter`.
                # (While defaultdict handles absence gracefully, `del` can
                # make comparisons more precise if s1_counter also doesn't
                # contain keys with 0 values).
                if window_counter[char_left] == 0:
                    del window_counter[char_left]

                # Move the `left` pointer one step to the right,
                # effectively shrinking the window.
                left += 1

            # --- Check for Permutation ---

            # After each window adjustment (expansion and potential shrinking),
            # we check if the character frequencies in our current window
            # exactly match the required frequencies from `s1_counter`.
            # If they match, it means we have found a permutation of `s1`
            # as a substring within `s2`.
            # The comparison `s1_counter == window_counter` works directly
            # for Counter objects (and defaultdicts behaving like Counters)
            # as it compares key-value pairs.
            if s1_counter == window_counter:
                return True

        # If the loop completes without finding any matching permutation,
        # it means no permutation of s1 exists as a substring in s2.
        return False

# --- Time and Space Complexity Analysis ---

# Time Complexity: O(L1 + L2)
# L1 = len(s1)
# L2 = len(s2)
#
# - Initializing s1_counter: O(L1) to iterate through s1.
# - The main loop iterates `right` from 0 to L2-1: O(L2) iterations.
# - Inside the loop:
#   - Adding `char_right` to window_counter: O(1) on average.
#   - The `while` loop (for shrinking): The `left` pointer also moves at most L2 times
#     across the entire execution. Each character from s2 is added and removed from
#     the window_counter at most once.
#   - Comparing `s1_counter == window_counter`: In the worst case, this involves
#     comparing up to 26 (for lowercase English alphabet) key-value pairs. So, O(1)
#     for a fixed alphabet size.
# Overall, since both `left` and `right` pointers traverse `s2` at most once,
# the operations inside the loop are effectively amortized O(1), leading to a total
# time complexity dominated by the lengths of the strings.

# Space Complexity: O(1)
#
# - s1_counter: Stores character frequencies for s1. Since s1 only contains
#   lowercase English letters, it will store at most 26 unique characters. So, O(26) which is O(1).
# - window_counter: Similarly, stores character frequencies for the current window in s2.
#   It will also store at most 26 unique characters. So, O(26) which is O(1).
# The space used does not grow with the input string lengths, only with the size of the alphabet.