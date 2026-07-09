from typing import List

class Solution:
    """
    Time Complexity: O(log N)
                     - The algorithm employs a binary search strategy on the input array `nums`.
                     - In each iteration of the `while` loop, the search space (defined by `left_pointer` and `right_pointer`)
                       is approximately halved.
                     - N represents the number of elements in the `nums` list.
                     - Therefore, the number of operations grows logarithmically with the size of the input.

    Space Complexity: O(1)
                      - The algorithm utilizes a constant amount of extra space.
                      - It only stores a few variables (`left_pointer`, `right_pointer`, `middle_index`, `middle_value`),
                        whose memory footprint does not depend on the size of the input array `nums`.
                      - No additional data structures (like lists, dictionaries, etc.) that scale with N are used.
    """
    def findMin(self, nums: List[int]) -> int:
        
        # Initialize the boundaries for the binary search.
        # `left_pointer`: Points to the start of the current search segment.
        #                 Initially, it's the first element's index (0).
        # `right_pointer`: Points to the end of the current search segment.
        #                  Initially, it's the last element's index (len(nums) - 1).
        left_pointer, right_pointer = 0, len(nums) - 1

        # `minimum_value_found`: This variable will store the potential minimum value.
        # It's initialized here, but its final value will be `middle_value` from the last
        # iteration when the loop condition `left_pointer <= right_pointer` is true.
        # Its scope needs to extend outside the loop for the final return.
        minimum_value_found = -1 # Placeholder; will be updated inside the loop

        # Perform a binary search. The loop continues as long as the `left_pointer`
        # is less than or equal to the `right_pointer`. This means there's a valid
        # search segment that could range from a single element to multiple elements.
        while left_pointer <= right_pointer:

            # Calculate the `middle_index` of the current search segment.
            # Using `(left_pointer + right_pointer) // 2` is a standard way to find the middle.
            # Python's integers handle arbitrary precision, so overflow is generally not a concern,
            # unlike in some other languages (e.g., C++ `(left + right) / 2`).
            middle_index = (left_pointer + right_pointer) // 2
            
            # Get the value at the `middle_index`.
            middle_value = nums[middle_index]

            # Store the `middle_value` as the current best candidate for the minimum.
            # This is crucial for the logic of `return minimum_value_found` outside the loop.
            # In the final iteration, `minimum_value_found` will hold the true minimum.
            minimum_value_found = middle_value 

            # Decision Point: Compare `middle_value` with `nums[right_pointer]`.
            # This comparison helps to identify which part of the array is sorted
            # and, consequently, where the minimum element must reside.
            if middle_value < nums[right_pointer]:
                # Scenario 1: `middle_value` is less than `nums[right_pointer]`.
                # This indicates that the sub-array from `middle_index` to `right_pointer`
                # is currently sorted in ascending order (or is a part of the sorted segment
                # that *doesn't* contain the pivot).
                # The minimum element, if it exists in this `[middle_index ... right_pointer]` segment,
                # must be `middle_value` itself.
                # Therefore, we narrow our search to the left half, *including* `middle_index`,
                # because `middle_value` is a candidate for the minimum.
                # We update `right_pointer` to `middle_index`.
                right_pointer = middle_index
            
            else: # This implicitly means `middle_value >= nums[right_pointer]`
                # Scenario 2: `middle_value` is greater than or equal to `nums[right_pointer]`.
                # This signifies that the rotation point (and thus the absolute minimum element)
                # *must* be located in the segment to the right of `middle_index`.
                # `middle_value` itself cannot be the minimum because there's `nums[right_pointer]`
                # which is smaller (or equal, in cases of duplicates not covered by original problem,
                # but for distinct elements, `middle_value > nums[right_pointer]`).
                # We safely discard `middle_index` and all elements to its left.
                # We update `left_pointer` to `middle_index + 1` to search in the right half,
                # excluding `middle_index`.
                left_pointer = middle_index + 1
        
        # When the `while` loop terminates, it means `left_pointer` has just become
        # greater than `right_pointer`. In the final iteration before termination,
        # `middle_index` would have pointed to the true minimum, and its value
        # would have been assigned to `minimum_value_found`.
        # Therefore, `minimum_value_found` correctly holds the minimum element
        # of the rotated sorted array.
        return minimum_value_found