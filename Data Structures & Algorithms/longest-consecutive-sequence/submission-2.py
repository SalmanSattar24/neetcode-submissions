from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
        The sequence must be consecutive (i.e., numbers appear in order without gaps), but the elements
        can be in any order in the input array.

        Approach:
        - Use a HashSet to store all numbers for O(1) lookups.
        - Iterate through the numbers and check if a number is the start of a sequence (i.e., num - 1 is not in the set).
        - If it's the start of a sequence, count the length by checking consecutive numbers in the set.
        - Track the maximum sequence length encountered.

        Complexity:
        - Time Complexity: O(N), since each number is processed once.
        - Space Complexity: O(N), due to storing numbers in a HashSet.

        Edge Cases:
        - If nums is empty, return 0.
        - If all numbers are unique but scattered, return the longest possible sequence.
        """

        if not nums:
            return 0  # If the input list is empty, return 0

        num_set = set(nums)  # Convert list to a set for O(1) lookups
        longest_sequence = 0  # Variable to track the longest consecutive sequence found

        for num in num_set:  # Iterate through unique numbers
            # Check if num is the start of a sequence (i.e., num - 1 is not in the set)
            if num - 1 not in num_set:
                current_length = 1  # Initialize sequence length
                current_num = num  # Start tracking the sequence

                # Expand the sequence by checking consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1  # Move to the next consecutive number
                    current_length += 1  # Increase sequence length

                # Update the longest sequence found so far
                longest_sequence = max(longest_sequence, current_length)

        return longest_sequence  # Return the length of the longest consecutive sequence
