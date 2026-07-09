class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Merges two sorted arrays `nums1` and `nums2` in-place into `nums1`.

        Args:
            nums1 (list[int]): The first sorted array with `m` valid elements and `n` placeholders (zeros).
            nums2 (list[int]): The second sorted array with `n` elements.
            m (int): Number of valid elements in `nums1`.
            n (int): Number of elements in `nums2`.

        Returns:
            None: Modifies `nums1` in-place.

        Time Complexity:
            O(m + n) - We iterate through both arrays once, placing elements in their correct positions.

        Space Complexity:
            O(1) - We modify `nums1` in-place without using extra space.
        """

        last = m + n - 1  # Pointer for the last position in `nums1`
        i, j = m - 1, n - 1  # Pointers for the last valid elements in `nums1` and `nums2`

        # Iterate while there are elements left in `nums2`
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:  # If `nums1[i]` is larger, place it at `nums1[last]`
                nums1[last] = nums1[i]  # Move the larger element to the correct position
                i -= 1  # Move `i` pointer left
            else:  # Otherwise, place `nums2[j]` at `nums1[last]`
                nums1[last] = nums2[j]  # Move `nums2[j]` to the correct position
                j -= 1  # Move `j` pointer left
            
            last -= 1  # Move `last` pointer left to fill the next position

        # No need to check `i >= 0` because remaining elements in `nums1` are already in place
