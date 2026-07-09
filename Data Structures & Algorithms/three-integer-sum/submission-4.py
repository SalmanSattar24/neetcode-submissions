from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in the array that sum up to zero.

        Time Complexity:
        - Sorting the array takes O(n log n).
        - The outer loop runs O(n) times.
        - The inner two-pointer search runs O(n) in the worst case.
        - Overall complexity: O(n^2).

        Space Complexity:
        - Sorting is done in-place, so no extra space is used.
        - The output list stores at most O(n^2) triplets in the worst case.
        - Overall space complexity: O(n^2) (for storing results).
        """

        # Sort the input array to facilitate two-pointer approach
        nums.sort()  # O(n log n) complexity

        # Result list to store unique triplets
        res = []

        # Iterate through the array, treating each element as a potential first number in the triplet
        for i in range(len(nums) - 2):  # O(n) complexity
            # Skip duplicate elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Ensures unique triplets

            # Initialize two pointers
            left, right = i + 1, len(nums) - 1

            # Two-pointer approach to find pairs that sum to -nums[i]
            while left < right:  # O(n) complexity per iteration
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    # Found a valid triplet, add to result
                    res.append([nums[i], nums[left], nums[right]])

                    # Move left pointer forward, skipping duplicates
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif total < 0:
                    # If sum is too small, move left pointer forward to increase sum
                    left += 1
                else:
                    # If sum is too large, move right pointer backward to decrease sum
                    right -= 1

        return res  # Final result containing all unique triplets
