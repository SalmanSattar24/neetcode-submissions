# Time Complexity: O(n), where n is the number of elements in the array.
# We iterate through the array at most once.
#
# Space Complexity: O(1).
# The algorithm modifies the input array in-place and does not use any additional
# data structures whose size scales with the input size.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Iterate through each number in the array.
        for num in nums:
            # We use the absolute value of the current number to get a corresponding
            # 0-indexed position. This works because all numbers are in the range [1, n].
            # We take the absolute value because we're modifying the array in-place
            # by negating values, so a number might already be negative.
            corresponding_index = abs(num) - 1

            # Check if the number at the corresponding index is already negative.
            # If it is, it means we have encountered this number before, as we
            # use negation as our "visited" marker.
            if nums[corresponding_index] < 0:
                # The current number is the duplicate, so we return its absolute value.
                return abs(num)
            
            # If the number at the corresponding index is not negative, it's the first time
            # we've seen this number. We mark it as "visited" by negating its value.
            # This mutation of the array serves as our hash set.
            nums[corresponding_index] *= -1