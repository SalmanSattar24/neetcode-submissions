from typing import List

class Solution:
    """
    This class provides a method to find the smallest missing positive integer
    in an unsorted array of integers.
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Finds the smallest positive integer (greater than 0) that does not
        exist in the input array `nums`.

        This algorithm operates in O(n) time complexity and O(1) extra space.
        It cleverly re-purposes the input array itself as a hash table to mark
        the presence of positive integers within the range [1, L], where L is
        the length of the array.

        The core strategy is built on these observations:
        1. The first missing positive integer must be within the range [1, L+1].
           If all numbers from 1 to L are present, then L+1 is the answer.
        2. We can use array indices to represent these positive integers.
           For example, index `0` can represent the number `1`, index `1` for `2`, and so on.
        3. The sign of the number at `nums[index]` can be used to indicate
           whether the number `(index + 1)` is present (negative sign) or missing (positive sign).
        """

        L = len(nums) # Get the length of the input array.

        # --- Phase 1: Normalize the array ---
        # The goal of this phase is to ensure that all elements that are not
        # relevant for finding the first missing positive (i.e., numbers
        # that are <= 0 or > L) are converted to a neutral value (0 in this case).
        # This prevents them from interfering with our marking scheme in Phase 2.
        for i in range(L):
            # If a number is negative, it's not a positive integer relevant to [1, L].
            # Replace it with 0.
            if nums[i] < 0:
                nums[i] = 0
            # Numbers greater than L are also irrelevant, but they are handled
            # implicitly in Phase 2 by `placement_index` checks.

        # --- Phase 2: Mark the presence of positive integers in range [1, L] ---
        # This is the "in-place hashing" part. We iterate through the modified array.
        # For each number `num` that is relevant (i.e., its absolute value is
        # within `[1, L]`), we go to its corresponding index and mark it negative.
        for i in range(L):
            # Take the absolute value of the current number.
            # This is important because `nums[i]` might already be negative
            # due to a previous marking in this phase.
            num = abs(nums[i])

            # Calculate the `placement_index`. For a positive integer `X`,
            # its "correct" sorted position (if it were 1-indexed) is `X`.
            # In a 0-indexed array, this corresponds to index `X - 1`.
            # E.g., `1` maps to index `0`, `2` maps to index `1`, etc.
            placement_index = num - 1

            # Check if `placement_index` is a valid index within the array bounds.
            # This ensures we only attempt to mark for numbers that fall within the range [1, L].
            # Numbers `> L` will have `placement_index >= L` and will be ignored.
            if 0 <= placement_index < L:
                # Case 1: The value at `nums[placement_index]` is currently positive.
                # This means the number `(placement_index + 1)` has *not yet been marked* as present.
                # We mark its presence by flipping the sign of the number at its corresponding index.
                # We multiply by -1 if it's strictly positive to avoid issues with 0.
                if nums[placement_index] > 0:
                    nums[placement_index] *= -1
                # Case 2: The value at `nums[placement_index]` is currently 0.
                # This `0` could be:
                #   a) An original `0` in the input array.
                #   b) A negative number that was converted to `0` in Phase 1.
                #
                # IMPORTANT: If a valid number `num` (from `nums[i]`) maps to this
                # `placement_index`, we *must* mark `(placement_index + 1)` as present.
                # Since multiplying `0` by `-1` still results in `0`, we need a different way
                # to mark it negative. We choose a distinct negative value: `-(L + 1)`.
                # This value is chosen to be outside the range of typical marked negatives
                # (-1 to -L), making it unequivocally a "marked present" indicator.
                elif nums[placement_index] == 0:
                    nums[placement_index] = -1 * (L + 1)
                # Note: If `nums[placement_index]` is already negative (e.g., another
                # occurrence of the same number, or a different number that mapped to
                # the same index), we do nothing, as it's already marked as present.

        # --- Phase 3: Find the first missing positive integer ---
        # Now, we iterate from `1` to `L` (inclusive), checking each positive integer
        # in this range. The state of `nums[index]` will tell us if `(index + 1)` is present.
        for i in range(1, L + 1):
            # Convert the 1-indexed number `i` to its 0-indexed array position.
            index = i - 1

            # The crucial check: `if nums[index] >= 0:`
            # Based on our marking scheme:
            # - If `nums[index]` is negative (e.g., -5, -(L+1)), it means the number
            #   `(index + 1)` was found and marked as present in Phase 2.
            # - If `nums[index]` is positive (> 0), it means the number `(index + 1)`
            #   was never encountered in the original `nums` array, and thus its
            #   corresponding index `nums[index]` was never marked negative.
            # - If `nums[index]` is 0: This is the important edge case we discussed.
            #   A `0` at `nums[index]` implies that the number `(index + 1)` was
            #   NOT present in the original array. If it *had* been present, and
            #   `nums[index]` was `0` when `(index + 1)` was processed, `nums[index]`
            #   would have been set to `-(L + 1)`. Since it remained `0`, it means
            #   no `num` mapped to this index to make it negative. Therefore, `(index + 1)`
            #   is indeed missing.
            #
            # Conclusion: Both positive values and `0` at `nums[index]` in this final
            # phase indicate that `(index + 1)` is a missing positive integer.
            # Thus, the condition `nums[index] >= 0` correctly identifies all such cases.
            if nums[index] >= 0:
                return i # `i` is the first positive integer that is missing.

        # --- Final Case: All numbers from 1 to L are present ---
        # If the loop completes without finding any `nums[index] >= 0`,
        # it means all numbers from 1 to L were found and marked as present
        # (i.e., `nums[0]` through `nums[L-1]` are all negative values).
        # In this scenario, the smallest missing positive integer is `L + 1`.
        return (L + 1)