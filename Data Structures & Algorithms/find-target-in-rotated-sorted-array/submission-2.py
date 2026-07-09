class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(log N)
        # The algorithm uses binary search, which repeatedly halves the search space.
        # This logarithmic time complexity is very efficient for large inputs.

        # Space Complexity: O(1)
        # The algorithm uses a constant amount of extra space regardless of the input size.
        # It only uses a few variables (left, right, mid, mid_num) to store indices and values.

        # Initialize left and right pointers for the binary search.
        # 'left' points to the first element (index 0).
        # 'right' points to the last element (index len(nums) - 1).
        left, right = 0, len(nums) - 1

        # The core of the binary search. The loop continues as long as
        # 'left' is less than or equal to 'right'. This ensures that
        # the search space is valid and includes single-element arrays.
        while left <= right:
            # Calculate the middle index. Using integer division (//)
            # ensures 'mid' is always an integer.
            mid = (left + right) // 2
            # Get the value at the middle index.
            mid_num = nums[mid]

            # Check if the middle element is the target.
            # If found, return its index immediately.
            if target == mid_num:
                return mid

            # Determine which half of the array is sorted.
            # This condition checks if the left half (from 'left' to 'mid')
            # is sorted.
            if nums[left] <= mid_num:
                # If the left half is sorted:
                # Check if the target is within the bounds of this sorted left half.
                # The target must be greater than 'mid_num' OR less than 'nums[left]'
                # to be in the UNSORTED (right) half.
                if target > mid_num or target < nums[left]:
                    # If the target is NOT in the sorted left half,
                    # discard the left half and search in the right half.
                    left = mid + 1
                else:
                    # If the target IS in the sorted left half,
                    # discard the right half and search in the left half.
                    right = mid - 1
            # If the left half is NOT sorted, it means the right half
            # (from 'mid' to 'right') must be sorted.
            else:
                # If the right half is sorted:
                # Check if the target is within the bounds of this sorted right half.
                # The target must be less than 'mid_num' OR greater than 'nums[right]'
                # to be in the UNSORTED (left) half.
                if target < mid_num or target > nums[right]:
                    # If the target is NOT in the sorted right half,
                    # discard the right half and search in the left half.
                    right = mid - 1
                else:
                    # If the target IS in the sorted right half,
                    # discard the left half and search in the right half.
                    left = mid + 1

        # If the loop finishes without finding the target,
        # it means the target is not present in the array.
        return -1