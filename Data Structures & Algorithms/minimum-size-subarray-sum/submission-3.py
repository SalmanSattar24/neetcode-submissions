from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        N = len(nums)

        - The 'right' pointer iterates through the `nums` array once: O(N) iterations.
        - The 'left' pointer also moves at most N times across the entire execution.
          Each element is added to `current_sum` once and subtracted from `current_sum`
          at most once.
        - All operations inside the loops (addition, subtraction, min comparison) are O(1).
        Therefore, the overall time complexity is linear with respect to the input array size.

        Space Complexity: O(1)
        - We are only using a few constant extra variables (`current_sum`, `left`,
          `min_subarray_len`, `right`).
        The space used does not grow with the input array size.
        """

        # Initialize current_sum to store the sum of elements in the current window.
        current_sum = 0

        # Initialize the left pointer of our sliding window.
        left = 0

        # Initialize min_subarray_len to a very large number (infinity).
        # This will store the smallest length of a subarray found so far
        # that satisfies the target sum condition.
        min_subarray_len = float('inf')

        # Iterate through the array using the 'right' pointer.
        # The 'right' pointer expands the window by including new elements.
        for right in range(len(nums)):
            # Add the element at the 'right' pointer to the current_sum.
            current_sum += nums[right]

            # This `while` loop is the core of shrinking the window.
            # It continues as long as two conditions are met:
            # 1. current_sum >= target: The current window's sum meets or exceeds the target.
            #    This means we have a candidate subarray.
            # 2. left <= right: Ensures the `left` pointer does not cross the `right` pointer,
            #    maintaining a valid window.
            while current_sum >= target and left <= right:
                # If the conditions are met, we have found a subarray that sums up to at least 'target'.
                # Calculate its length: (right - left + 1).
                # Update min_subarray_len if this current subarray is shorter than any found before.
                min_subarray_len = min(min_subarray_len, right - left + 1)

                # Now, to find an even smaller subarray, we try to shrink the window
                # from the left by removing the element at the `left` pointer.
                current_sum -= nums[left]

                # Move the `left` pointer one step to the right.
                # This effectively removes `nums[left]` from the window.
                left += 1

        # After iterating through all possible windows:
        # If `min_subarray_len` is still `float('inf')`, it means no subarray
        # was found that sums up to at least the `target`. In this case, return 0.
        # Otherwise, return the `min_subarray_len` found.
        return 0 if min_subarray_len == float('inf') else min_subarray_len