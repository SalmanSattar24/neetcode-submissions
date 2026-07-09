from collections import Counter, defaultdict

class Solution:
    """
    Time Complexity: O(n)
        - The 'right' pointer iterates through the string 's' once, taking O(n) time.
        - The 'left' pointer, in the 'while' loop, also iterates through the string 's' at most once
          (it only moves forward).
        - Dictionary operations (get, put, delete) for Counter and defaultdict take O(1) on average.
        - Therefore, each character of 's' is processed by both 'left' and 'right' pointers at most
          a constant number of times.
    Space Complexity: O(k)
        - Where 'k' is the number of unique characters in the input string 't'.
        - 'counter_t' stores frequencies for characters in 't', taking O(k) space.
        - 'window_counter' stores frequencies for characters in the current window, also taking
          O(k) space in the worst case (if all unique characters from 's' are in 't' or are processed).
        - In the context of ASCII or Unicode character sets, 'k' is at most 256 or 128, making it
          effectively O(1) if the character set size is considered constant.
    """
    def minWindow(self, s: str, t: str) -> str:
        # If 't' is an empty string, no substring is needed, so return an empty string.
        if not t:
            return ""

        # Create a frequency map for characters in string 't'.
        # This tells us what characters we 'need' and in what quantities.
        counter_t = Counter(t)
        
        # Create a frequency map for characters currently within our sliding window in string 's'.
        # Using defaultdict(int) automatically initializes new keys with a value of 0.
        window_counter = defaultdict(int)
        
        # 'have' tracks how many unique characters from 't' (with their required frequencies)
        # are currently satisfied within the 'window_counter'.
        # 'need' is the total number of unique characters in 't' that we must satisfy.
        have, need = 0, len(counter_t) 

        # 'res' will store the start and end indices of the minimum window found so far.
        # Initialized to [-1, -1] to indicate no valid window found yet.
        # 'min_len' stores the length of the shortest valid window found.
        # Initialized to float('inf') to ensure any valid window length will be smaller.
        res, min_len = [-1, -1], float('inf')
        
        # 'left' is the left pointer of the sliding window.
        left = 0

        # Iterate with the 'right' pointer to expand the window.
        for right in range(len(s)):
            char_right = s[right] # Get the character at the right pointer.
            
            # Add the current character to the window's frequency count.
            window_counter[char_right] += 1 

            # Check if this character is one we need from 't' AND
            # if its current count in the window now matches the required count in 't'.
            # If both conditions are true, it means we've successfully 'matched' this character's requirement.
            if char_right in counter_t and window_counter[char_right] == counter_t[char_right]:
                have += 1 # Increment 'have' count, as one more character requirement is met.
            
            # This 'while' loop is executed when the current window is "valid", meaning it contains
            # all characters from 't' with at least their required frequencies.
            # We try to shrink the window from the left to find the smallest valid window.
            while have == need:
                current_len = right - left + 1 # Calculate the length of the current valid window.
                
                # If this current valid window is shorter than the minimum found so far, update.
                if current_len < min_len:
                    min_len = current_len # Update the minimum length.
                    res = [left, right] # Store the start and end indices of this shorter window.

                char_left = s[left] # Get the character at the left pointer.
                
                # Decrement the count of the character leaving the window.
                window_counter[char_left] -= 1

                # If the character leaving the window was one that was required by 't' AND
                # its count in the window now falls below the required count in 't',
                # it means this character's requirement is no longer fully satisfied.
                if char_left in counter_t and window_counter[char_left] < counter_t[char_left]:
                    have -= 1 # Decrement 'have' as one requirement is no longer met.
                
                left += 1 # Shrink the window by moving the left pointer to the right.
        
        # After iterating through the entire string 's', 'res' holds the indices
        # of the shortest valid window, if one was found.
        start, end = res
        
        # If 'min_len' is still float('inf'), it means no valid window was ever found.
        # Otherwise, reconstruct and return the substring from 's' using the stored indices.
        # 'end + 1' is used because string slicing in Python is exclusive of the end index.
        return s[start : end + 1] if min_len != float('inf') else ""