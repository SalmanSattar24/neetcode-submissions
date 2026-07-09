from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place and returns the count of unique elements.

        Args:
            nums (List[int]): The input sorted array.

        Returns:
            int: The number of unique elements in `nums`.

        Time Complexity:
            O(N) - We iterate through the array once.

        Space Complexity:
            O(1) - We modify the array in-place without extra storage.
        """

        if not nums:  # Edge case: If the array is empty, return 0
            return 0

        left = 0  # Pointer to track the position of unique elements

        # Iterate through the array starting from the second element
        for right in range(1, len(nums)):  
            if nums[left] != nums[right]:  # If a new unique element is found
                left += 1  # Move the `left` pointer forward
                nums[left] = nums[right]  # Place the unique element at the correct position

        return left + 1  # Return the count of unique elements (index + 1)
