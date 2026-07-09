from collections import defaultdict
from typing import List

class Solution:
    """
    This class provides a method to find all elements that appear more than ⌊n/3⌋ times
    in an integer array. This is a variation of the Majority Element problem.
    """

    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Finds all elements that appear more than ⌊n/3⌋ times in the input list.

        This implementation uses a modified Boyer-Moore majority vote algorithm
        to efficiently track potential majority elements, followed by a final
        verification step. The Boyer-Moore algorithm is adapted to handle
        up to two majority elements since at most two elements can appear
        more than n/3 times in an array of length n.

        Args:
            nums: A list of integers.

        Returns:
            A list of integers representing the majority elements.
        """

        # Initialize a defaultdict to store the counts of potential majority elements.
        # A defaultdict is used because it provides a default value (0 in this case)
        # for a key that does not exist, simplifying the counting process.
        count = defaultdict(int)

        # --- Phase 1: Finding Potential Majority Candidates (Modified Boyer-Moore) ---
        # This loop iterates through each number in the input list to identify
        # candidates for majority elements. The key idea is to maintain counts
        # for at most two distinct elements. If a third distinct element is encountered,
        # we decrement the counts of all existing candidates. This effectively
        # "cancels out" elements that are not majority elements.
        for num in nums:
            # Increment the count for the current number.
            count[num] += 1

            # If the number of distinct elements being tracked (keys in 'count')
            # is 3 or more, it means we've encountered too many distinct candidates.
            # In this case, we need to "reduce" the counts by simulating removals
            # or cancellations. This is crucial for the Boyer-Moore-like approach.
            if len(count) > 2:
                # Create a new defaultdict to store the updated counts.
                new_count = defaultdict(int)

                # Iterate through the current potential candidates and their frequencies.
                for val, freq in count.items():
                    # If an element's frequency is greater than 1, it means it
                    # still has a "vote" remaining after cancellation.
                    # We decrement its count by 1 (simulating cancellation with the new element).
                    if freq > 1:
                        new_count[val] = freq - 1

                # Replace the old 'count' with the 'new_count'. This effectively
                # discards elements whose counts dropped to zero and updates
                # the counts of the remaining potential candidates.
                count = new_count

        # --- Phase 2: Verification of Potential Majority Candidates ---
        # After the first pass, the 'count' dictionary contains at most two
        # elements that are *potential* majority elements. It's crucial to
        # verify these candidates because the Boyer-Moore algorithm only
        # guarantees that if a majority element exists, it will be among the
        # candidates. It does not guarantee that all candidates are majority elements.

        # Initialize an empty list to store the final majority elements.
        res = []

        # Calculate the threshold for a majority element. An element is a majority
        # element if its count is greater than floor(n/3).
        majority_threshold = len(nums) // 3

        # Iterate through the potential majority elements found in Phase 1 (keys in 'count').
        for num in count:
            # For each potential candidate, count its actual occurrences in the original 'nums' list.
            # This step is necessary to confirm if it truly meets the majority criteria.
            # The `nums.count(num)` method iterates through the entire list again.
            if nums.count(num) > majority_threshold:
                # If the actual count of the number is greater than the majority threshold,
                # then it is indeed a majority element. Add it to the result list.
                res.append(num)

        # Return the list of verified majority elements.
        return res