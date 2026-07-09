from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Checks if there are two distinct indices i and j in the array `nums`
        such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

        This solution uses a sliding window approach with a hash set (Python's set).

        Args:
            nums (List[int]): The input list of integers.
            k (int): The maximum allowed difference between indices.

        Returns:
            bool: True if such a duplicate exists within the window of size k, False otherwise.

        Time Complexity: O(N)
            - The code iterates through the `nums` array once using the `right` pointer.
            - Inside the loop, set operations (`add`, `remove`, `in`) take
              average O(1) time.
            - In the worst case, each element is added and removed from the set once.
            Therefore, the overall time complexity is O(N).

        Space Complexity: O(min(N, K))
            - The `window_elements` set stores elements within the current sliding window.
            - The maximum size of this window (and thus the set) is `k + 1`.
            - In the worst case, if all elements are unique within the window, the set
              will store up to `k + 1` elements.
            - The maximum possible size of the set is `N` (if `k` is very large, i.e., `k >= N`).
            Therefore, the space complexity is bounded by the smaller of N and K.
        """

        # `window_elements` will store the unique elements currently within our sliding window.
        # Using a set provides O(1) average time complexity for lookups, additions, and removals.
        window_elements = set()

        # `left_pointer` marks the beginning of our sliding window.
        left_pointer = 0

        # Iterate through the array with `right_pointer` to expand the window.
        for right_pointer in range(len(nums)):
            # Check if the window size (right_pointer - left_pointer) exceeds k.
            # If it does, we need to shrink the window from the left.
            if right_pointer - left_pointer > k:
                # Remove the element at the `left_pointer` from the window,
                # as it's now outside the valid `k` range.
                window_elements.remove(nums[left_pointer])
                # Move the `left_pointer` one step to the right to shrink the window.
                left_pointer += 1

            # Check if the current element at `right_pointer` is already present
            # in our `window_elements` set.
            # If it is, we've found a duplicate within the `k` distance.
            if nums[right_pointer] in window_elements:
                return True # Found a duplicate within k distance, so return True.

            # If no duplicate was found for the current `nums[right_pointer]`,
            # add it to the `window_elements` set for future checks.
            window_elements.add(nums[right_pointer])

        # If the loop completes without finding any duplicate within the `k` distance,
        # it means no such duplicate exists.
        return False
        