from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # char_counter: A dictionary (using defaultdict for convenience) to store
        # the frequency of each character within the current sliding window.
        # It's initialized with 'int' so that accessing a new key automatically
        # creates it with a default value of 0.
        char_counter = defaultdict(int)

        # left: The left pointer of our sliding window. It marks the beginning
        # of the current substring we are considering.
        left = 0

        # max_len: This variable will store the maximum length of a valid
        # repeating character substring found so far. This is our final answer.
        max_len = 0

        # max_freq: This variable keeps track of the highest frequency of
        # any single character encountered within the *current* sliding window.
        # This is crucial for calculating the number of replacements needed.
        max_freq = 0

        # Iterate through the string using the 'right' pointer to expand the window.
        # The 'right' pointer effectively defines the right boundary of our current window.
        for right in range(len(s)):
            # Get the character at the 'right' pointer.
            char = s[right]

            # Increment the count of the current character in our frequency map.
            # This character is now part of our sliding window.
            char_counter[char] += 1

            # Update max_freq. We take the maximum of the current max_freq and
            # the frequency of the character just added. This ensures max_freq
            # always reflects the count of the most frequent character in the
            # window from 'left' to 'right'.
            max_freq = max(max_freq, char_counter[char])

            # This `while` loop is the core of the sliding window logic for this problem.
            # It checks if the current window is "valid" based on the 'k' replacements allowed.

            # The condition: (window_length - max_freq) > k
            #
            # - (right - left + 1): This is the current length of our sliding window.
            #   For example, if right=3 and left=0, window length is 3 - 0 + 1 = 4.
            #
            # - max_freq: This is the count of the most frequent character in the current window.
            #
            # - (window_length - max_freq): This crucial calculation tells us
            #   how many characters in the *current window* are *not* the most frequent character.
            #   These are precisely the characters that we would need to *replace*
            #   to make the entire window consist of only the most frequent character.
            #
            # - If this number of replacements needed is GREATER THAN 'k' (the allowed replacements),
            #   then our current window is INVALID. We must shrink it from the left.
            while (right - left + 1) - max_freq > k:
                # Get the character that is currently at the 'left' end of the window.
                left_char = s[left]

                # Decrement its count in the frequency map because it's about to
                # be removed from our sliding window as we shrink.
                char_counter[left_char] -= 1

                # Move the 'left' pointer one step to the right, effectively shrinking the window.
                left += 1

                # --- IMPORTANT EXPLANATION: Why we don't recalculate max_freq here ---
                # When the window shrinks, we might be tempted to re-calculate `max_freq`
                # by iterating through `char_counter` or by checking if `left_char` was
                # the `max_freq` character. However, this is generally not necessary
                # for the correctness and efficiency of this specific sliding window approach.
                #
                # Here's why:
                # 1. `max_freq` as a "High Water Mark": `max_freq` is always updated when the
                #    window *expands* (`right` pointer moves). This means it always holds
                #    the maximum frequency encountered *so far* within any window that has
                #    included the characters up to the current `right` pointer.
                #    It effectively acts as a "high water mark."
                #
                # 2. Focus on Window Validity: The `while` loop's primary purpose is
                #    to ensure that the *current window* is valid with respect to `k`.
                #    When `left` moves, the window length `(right - left + 1)` *decreases*.
                #    If `max_freq` stays the same (even if it's no longer the absolute max
                #    in the now-smaller window), the term `(right - left + 1) - max_freq`
                #    will also *decrease*.
                #
                # 3. Guaranteed Convergence: The crucial point is that by continuously
                #    decreasing `(right - left + 1)`, we are guaranteed that eventually
                #    the condition `(right - left + 1) - max_freq > k` will become `False`.
                #    Even if `max_freq` itself is no longer truly the maximum frequency
                #    in the *shrunken* window, the reduction in `window_length` will
                #    eventually satisfy the condition. The goal is to make the `replacements needed`
                #    less than or equal to `k`, and shrinking the window accomplishes this
                #    whether `max_freq` is perfectly precise or just a valid upper bound
                #    for the purposes of satisfying the `while` condition.
                #
                # 4. We Only Care About the Max Valid Length: The `max_len` is updated
                #    *after* the `while` loop has completed, i.e., after the window has
                #    been made valid. At this point, `(right - left + 1)` is a valid
                #    window length. Since we are interested in the *overall maximum* valid
                #    length, we don't need to worry about intermediate `max_freq` values
                #    during shrinking affecting the final result, as long as the shrinking
                #    process correctly identifies a valid window.
                #
                # This optimization (not recalculating `max_freq` when shrinking)
                # helps maintain the O(N) time complexity. If we recalculated `max_freq`
                # on every shrink, it could potentially involve iterating through `char_counter`,
                # leading to worse performance in some cases.
                #
                # The `max_freq` value becomes perfectly accurate again when the `right`
                # pointer moves and the `max_freq = max(max_freq, char_counter[char])`
                # line is executed.

            # After the `while` loop, the current window (from `left` to `right`)
            # is guaranteed to be a valid one (i.e., (window_length - max_freq) <= k).
            # We update `max_len` with the current window's length if it's greater
            # than the previously recorded maximum.
            max_len = max(max_len, (right - left + 1))

        # After iterating through the entire string, max_len will hold the
        # length of the longest substring meeting the criteria.
        return max_len