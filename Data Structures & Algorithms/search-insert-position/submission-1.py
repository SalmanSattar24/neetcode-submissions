from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search for O(log n) insertion index
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]

            if mid_val == target:
                # Found target at mid index
                return mid
            elif mid_val < target:
                # Target lies to the right of mid
                left = mid + 1
            else:
                # Target lies to the left of mid
                right = mid - 1

        # If not found, left will be the correct insertion point
        return left
