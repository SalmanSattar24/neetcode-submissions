from typing import List

class Solution:
    """
    This class provides a method to find the total number of continuous subarrays
    whose sum equals a given integer k.
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Calculates the total number of continuous subarrays whose sum equals k.

        This method utilizes the prefix sum technique combined with a hash map
        (dictionary in Python) to efficiently count the subarrays. It handles
        both positive and negative numbers in the input array.

        The core idea is:
        If `sum[i...j]` is the sum of elements from index `i` to `j`,
        then `sum[i...j] = sum[0...j] - sum[0...i-1]`.
        We are looking for subarrays where `sum[i...j] = k`.
        So, `k = sum[0...j] - sum[0...i-1]`.
        Rearranging this, we get `sum[0...i-1] = sum[0...j] - k`.

        This means, for every `current_sum` (which is `sum[0...j]`), if we
        have previously encountered a `prefix_sum` equal to `current_sum - k`,
        then the subarray between that `prefix_sum`'s end index and the current
        index `j` will sum up to `k`.

        Args:
            nums: A list of integers representing the input array.
            k: The target sum for the subarrays.

        Returns:
            An integer representing the total number of subarrays whose sum equals k.
        """

        # Initialize a dictionary (hash map) to store the frequencies of prefix sums.
        # The key is the prefix sum, and the value is the number of times that
        # prefix sum has been encountered so far.
        # We initialize `prefix_sums = {0: 1}`. This is a crucial step.
        # It handles the case where a subarray itself, starting from index 0,
        # sums up to `k`. If `current_sum - k` becomes `0`, and we haven't seen `0`
        # as a prefix sum before, it means the current `current_sum` itself is `k`.
        # By setting `0: 1`, we account for this scenario correctly.
        prefix_sums = {0: 1}

        # `cur_sum` keeps track of the sum of elements from the beginning of the
        # array up to the current element being processed. This is our `sum[0...j]`.
        cur_sum = 0

        # `res` will store the final count of subarrays whose sum equals k.
        res = 0

        # Iterate through each number in the input array `nums`.
        for num in nums:
            # Update `cur_sum` by adding the current number.
            cur_sum += num

            # Calculate `diff`. This `diff` represents the `sum[0...i-1]` we are looking for.
            # If `diff` exists as a key in `prefix_sums`, it means there's a previous
            # prefix sum that, when subtracted from the `current_sum`, yields `k`.
            diff = cur_sum - k

            # Check if `diff` exists in `prefix_sums`.
            # `prefix_sums.get(diff, 0)` safely retrieves the count of `diff`.
            # If `diff` is not found, it returns `0`.
            # Add the count of `diff` to `res`. Each occurrence of `diff` means
            # one valid subarray ending at the current position.
            res += prefix_sums.get(diff, 0)

            # Update the `prefix_sums` dictionary with the `current_sum`.
            # Increment the count for the `current_sum`. If `current_sum` is
            # encountered for the first time, `get(cur_sum, 0)` will return 0,
            # and it will be initialized to 1. Otherwise, its count is incremented.
            # This line should be:
            # prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
            #
            # The original code has a subtle bug here:
            # prefix_sums[cur_sum] = prefix_sums.get(diff, 0) + 1
            # This line is incorrectly using `diff` instead of `cur_sum` for the `get` method.
            # It should always increment the count of the *current* prefix sum.
            # Let's assume the correct line for the comments below.

            # Corrected line for the `prefix_sums` update:
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1


        # After iterating through all numbers, `res` will hold the total count
        # of subarrays that sum up to `k`.
        return res