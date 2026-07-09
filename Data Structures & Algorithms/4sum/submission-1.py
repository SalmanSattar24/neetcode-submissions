from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique quadruplets in the array that sum up to the target.

        Time Complexity:
        - Sorting the array takes O(n log n).
        - The recursive kSum function runs O(n^(k-1)) times.
        - Overall complexity: O(n^3) for 4Sum.

        Space Complexity:
        - Sorting is done in-place, so no extra space is used.
        - The output list stores at most O(n^2) quadruplets in the worst case.
        - Overall space complexity: O(n^2) (for storing results).
        """

        # Sort the input array to facilitate two-pointer approach
        nums.sort()  # O(n log n) complexity

        # Result list to store unique quadruplets
        res = []

        def kSum(k, start, target):
            """
            Recursive function to find k numbers that sum to target.
            Uses two-pointer approach when k == 2.
            """
            if k == 2:
                # Two-pointer approach for 2Sum
                left, right = start, len(nums) - 1

                while left < right:
                    summ = nums[left] + nums[right]

                    if summ < target:
                        left += 1  # Increase left pointer to get a larger sum
                    elif summ > target:
                        right -= 1  # Decrease right pointer to get a smaller sum
                    else:
                        # Found a valid pair, add to result
                        res.append(quad + [nums[left], nums[right]])

                        # Move both pointers to avoid duplicates
                        left += 1
                        right -= 1

                        # Skip duplicate values for left pointer
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                return

            # Iterate through the array, treating each element as a potential first number in the kSum
            for i in range(start, len(nums) - k + 1):
                # Skip duplicate elements to avoid duplicate results
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Add current number to the quad list
                quad.append(nums[i])

                # Recursively call kSum for k-1 numbers
                kSum(k - 1, i + 1, target - nums[i])

                # Remove last element to backtrack
                quad.pop()

        # Initialize quad list for storing intermediate results
        quad = []
        kSum(4, 0, target)

        return res  # Final result containing all unique quadruplets
