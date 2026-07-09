from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts an array containing only 0s, 1s, and 2s in-place.
        This is often referred to as the Dutch National Flag problem.
        The colors are typically represented as: 0 (red), 1 (white), and 2 (blue).
        The array should be sorted such that all 0s come first, then all 1s,
        and finally all 2s.

        The method should modify the 'nums' list in-place and not return anything.

        Two approaches are shown:
        1. Two-pass counting sort (currently active in the provided snippet).
        2. One-pass three-pointer approach (Dutch National Flag algorithm - commented out).
        """

        # --- Approach 1: Two-Pass Counting Sort ---
        # This approach first counts the occurrences of each color (0, 1, 2)
        # and then overwrites the array with the sorted colors based on these counts.

        # Initialize counters for each color.
        red_count = 0    # Counter for 0s
        white_count = 0  # Counter for 1s
        blue_count = 0   # Counter for 2s

        # First pass: Count the occurrences of each color.
        for color in nums:
            if color == 0:
                red_count += 1
            elif color == 1:
                white_count += 1
            else: # color must be 2
                blue_count += 1

        # Second pass: Overwrite the original 'nums' array with the sorted colors.
        # Iterate through the array indices to place the colors.
        current_index = 0

        # Place all the red (0) balls.
        for _ in range(red_count):
            nums[current_index] = 0
            current_index += 1

        # Place all the white (1) balls.
        for _ in range(white_count):
            nums[current_index] = 1
            current_index += 1

        # Place all the blue (2) balls.
        for _ in range(blue_count):
            nums[current_index] = 2
            current_index += 1

        # The array 'nums' is now sorted in-place. No return value is needed.

        # --- Approach 2: One-Pass Three-Pointer (Dutch National Flag Algorithm) ---
        # This approach sorts the array in a single pass using three pointers.
        # It's generally more efficient as it avoids the second pass of overwriting.
        # This section was commented out in the original prompt, but comments are added for completeness.

        # # 'p0' points to the boundary of the 0s section (all elements to the left of p0 are 0s).
        # # It starts at the beginning of the array.
        # p0 = 0

        # # 'p2' points to the boundary of the 2s section (all elements to the right of p2 are 2s).
        # # It starts at the end of the array.
        # p2 = len(nums) - 1

        # # 'curr' is the current element being considered. It iterates from the beginning
        # # towards p2.
        # curr = 0

        # # The loop continues as long as the current pointer 'curr' has not surpassed
        # # the pointer for the 2s section 'p2'.
        # # The region between 'p0' and 'curr-1' contains 1s that are in their correct place (for now).
        # # The region between 'curr' and 'p2' is the unsorted part we are currently processing.
        # while curr <= p2:
        #     # Case 1: If the current element is 0 (red).
        #     if nums[curr] == 0:
        #         # Swap nums[curr] with nums[p0]. This moves the 0 to its correct sorted region.
        #         nums[curr], nums[p0] = nums[p0], nums[curr]
        #         # Increment 'p0' because the 0s section has expanded.
        #         p0 += 1
        #         # Increment 'curr' because the element at 'curr' (which was swapped from p0)
        #         # has now been processed or needs to be processed.
        #         # If nums[p0] was a 0, curr moves past it. If it was a 1, it's in a good spot for now.
        #         curr += 1

        #     # Case 2: If the current element is 2 (blue).
        #     elif nums[curr] == 2:
        #         # Swap nums[curr] with nums[p2]. This moves the 2 to its correct sorted region.
        #         nums[curr], nums[p2] = nums[p2], nums[curr]
        #         # Decrement 'p2' because the 2s section has expanded from the right.
        #         p2 -= 1
        #         # IMPORTANT: Do NOT increment 'curr' here.
        #         # The element swapped from nums[p2] to nums[curr] has not yet been processed.
        #         # It could be a 0, 1, or another 2, so it needs to be re-evaluated in the next iteration.

        #     # Case 3: If the current element is 1 (white).
        #     else: # nums[curr] == 1
        #         # The element is a 1. It's in the "correct" place relative to 0s and 2s
        #         # for the current partitioning. We just move to the next element.
        #         curr += 1
        #
        # # After the loop, the array 'nums' is sorted in-place.

# Algorithm Explanation (Approach 1: Two-Pass Counting Sort):
# 1. Count Frequencies: Iterate through the array once to count how many 0s, 1s, and 2s exist.
# 2. Overwrite Array: Iterate through the array positions again.
#    a. Fill the beginning of the array with the counted number of 0s.
#    b. Then, fill the next part with the counted number of 1s.
#    c. Finally, fill the remaining part with the counted number of 2s.
# This is simple but requires two passes over the data (or one pass and then constructing based on counts).

# Algorithm Explanation (Approach 2: One-Pass Three-Pointer - Dutch National Flag):
# 1. Pointers: Maintain three pointers:
#    - `p0`: Marks the end of the 0s region (elements `nums[0...p0-1]` are 0s).
#    - `curr`: The current element being examined.
#    - `p2`: Marks the beginning of the 2s region (elements `nums[p2+1...end]` are 2s).
#    The region `nums[p0...curr-1]` will contain 1s.
#    The region `nums[curr...p2]` is the "unknown" or "to be processed" region.
# 2. Iteration: Iterate with `curr` as long as `curr <= p2`.
#    - If `nums[curr]` is 0: Swap `nums[curr]` with `nums[p0]`. Increment both `p0` and `curr`.
#    - If `nums[curr]` is 2: Swap `nums[curr]` with `nums[p2]`. Decrement `p2`. (Do NOT increment `curr`
#      because the new `nums[curr]` needs to be processed).
#    - If `nums[curr]` is 1: It's in the correct relative place for now. Increment `curr`.
# This sorts the array in a single pass.

# Example (Approach 1): nums = [2,0,2,1,1,0]
# 1. Counts: red=2, white=2, blue=2
# 2. Overwrite:
#    nums[0]=0, red=1
#    nums[1]=0, red=0
#    nums[2]=1, white=1
#    nums[3]=1, white=0
#    nums[4]=2, blue=1
#    nums[5]=2, blue=0
# Result: [0,0,1,1,2,2]

# Example (Approach 2): nums = [2,0,2,1,1,0]
# Initial: p0=0, curr=0, p2=5. nums=[2,0,2,1,1,0]
# curr=0, nums[0]=2: Swap nums[0],nums[5] -> [0,0,2,1,1,2]. p2=4. curr not incremented.
# curr=0, nums[0]=0: Swap nums[0],nums[0] -> [0,0,2,1,1,2]. p0=1, curr=1.
# curr=1, nums[1]=0: Swap nums[1],nums[1] -> [0,0,2,1,1,2]. p0=2, curr=2.
# curr=2, nums[2]=2: Swap nums[2],nums[4] -> [0,0,1,1,2,2]. p2=3. curr not incremented.
# curr=2, nums[2]=1: curr=3.
# curr=3, nums[3]=1: curr=4.
# curr=4, nums[4]=2: (curr > p2 is false, 4 > 3 is true). Loop terminates. (Error in manual trace, should be curr <= p2)
# Let's re-trace Approach 2 more carefully:
# Initial: nums=[2,0,2,1,1,0], p0=0, curr=0, p2=5
# 1. curr=0, nums[0]=2. Swap nums[0] with nums[5] -> [0,0,2,1,1,2]. p2=4. curr=0.
# 2. curr=0, nums[0]=0. Swap nums[0] with nums[0] -> [0,0,2,1,1,2]. p0=1, curr=1.
# 3. curr=1, nums[1]=0. Swap nums[1] with nums[1] -> [0,0,2,1,1,2]. p0=2, curr=2.
# 4. curr=2, nums[2]=2. Swap nums[2] with nums[4] -> [0,0,1,1,2,2]. p2=3. curr=2.
# 5. curr=2, nums[2]=1. (It's a 1). curr=3.
# 6. curr=3, nums[3]=1. (It's a 1). curr=4.
# 7. curr=4. Now curr > p2 (4 > 3). Loop terminates.
# Result: [0,0,1,1,2,2]

# Time Complexity:
# - Approach 1: O(N) for counting + O(N) for overwriting = O(N).
# - Approach 2: O(N) because each element is visited by `curr` at most a few times (due to swaps).
# Space Complexity:
# - Approach 1: O(1) if we consider the counters as constant space (or O(K) if K is number of colors).
# - Approach 2: O(1) as it's an in-place sort.
