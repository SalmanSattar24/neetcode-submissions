class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Time Complexity: O(log N) on average, O(N) in the worst case.
        # This algorithm is based on binary search, which generally offers logarithmic time complexity
        # (O(log N)) because it repeatedly halves the search space.
        # However, the presence of duplicate elements can degrade the worst-case performance to O(N).
        # This occurs when `nums[left]`, `nums[mid]`, and `nums[right]` are all identical.
        # In such scenarios (e.g., [1,1,1,0,1,1,1]), the algorithm cannot definitively determine
        # which half is sorted or where the rotation point is. To proceed, it must
        # linearly shrink the search space by moving 'left' and 'right' inwards.
        # If this happens repeatedly for a significant portion of the array, it can
        # effectively become a linear scan, leading to O(N) complexity.

        # Space Complexity: O(1)
        # The algorithm uses a constant amount of extra space, irrespective of the input array's size.
        # It only utilizes a few variables (left, right, mid) to store indices and values.
        # No additional data structures are created that scale with the input 'N'.

        # Initialize 'left' and 'right' pointers to define the current search space.
        # 'left' points to the first element (index 0).
        # 'right' points to the last element (index len(nums) - 1).
        left, right = 0, len(nums) - 1

        # The main binary search loop.
        # The loop continues as long as 'left' is less than or equal to 'right'.
        # This condition is crucial for a few reasons:
        # 1. It ensures the search space [left, right] remains valid.
        # 2. It allows the loop to execute even when only a single element is left
        #    in the search space (i.e., when 'left' and 'right' point to the same index),
        #    ensuring that this last element is checked.
        while left <= right:
            # Calculate the middle index of the current search segment.
            # Using integer division `//` ensures `mid` is always a whole number.
            # This calculation method also helps prevent potential integer overflow
            # that might occur with `(left + right)` in some programming environments.
            mid = (left + right) // 2

            # Check if the middle element is the target.
            # If the target is found, we immediately return True, as the problem
            # asks for a boolean result indicating presence.
            if nums[mid] == target:
                return True

            # Handle the specific case of duplicate values that makes this problem
            # distinct from "Search in Rotated Sorted Array I".
            # If `nums[left]`, `nums[mid]`, and `nums[right]` are all identical,
            # we cannot effectively use the values to determine which half is sorted.
            # Example: `nums = [1, 1, 1, 0, 1]` with `left=0`, `mid=2`, `right=4`.
            # In this scenario, we safely shrink the search space by moving both
            # 'left' and 'right' pointers inward by one position. This helps to
            # bypass segments of duplicate values that hinder the binary search logic.
            # This is the part that can lead to O(N) worst-case time complexity.
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue # Skip the rest of the loop and re-evaluate with new 'left'/'right'

            # Determine which half of the array is sorted.
            # This condition checks if the segment from 'left' to 'mid' is sorted.
            # We use `<=` here because `nums[left]` could be equal to `nums[mid]`
            # if they are part of a sorted segment that includes duplicates (e.g., [3,3,4,5,1,2]).
            if nums[left] <= nums[mid]:
                # If the left half (`nums[left]` to `nums[mid]`) is sorted:
                # Now, check if the `target` falls within the range of this sorted left half.
                # `nums[left] <= target` ensures the target is not smaller than the minimum value in this sorted part.
                # `target < nums[mid]` ensures the target is not greater than the maximum value
                # (excluding `nums[mid]` itself, which was already checked).
                if nums[left] <= target < nums[mid]:
                    # If the target is within the sorted left half,
                    # we discard the right half and narrow our search to the left half.
                    right = mid - 1
                else:
                    # If the target is NOT in the sorted left half,
                    # it must be in the (potentially unsorted or rotated) right half.
                    # Discard the left half and narrow our search to the right half.
                    left = mid + 1
            # If `nums[left] > nums[mid]`, it means the left half is NOT sorted in ascending order.
            # This implies that the pivot (rotation point) must lie within the left segment
            # or before `mid`. Consequently, the right half (`nums[mid]` to `nums[right]`)
            # must be sorted.
            else:
                # If the right half (`nums[mid]` to `nums[right]`) is sorted:
                # Check if the `target` falls within the range of this sorted right half.
                # `nums[mid] < target` ensures the target is not smaller than the minimum value in this sorted part.
                # `target <= nums[right]` ensures the target is not greater than the maximum value in this sorted part.
                if nums[mid] < target <= nums[right]:
                    # If the target is within the sorted right half,
                    # discard the left half and narrow our search to the right half.
                    left = mid + 1
                else:
                    # If the target is NOT in the sorted right half,
                    # it must be in the (potentially unsorted or rotated) left half.
                    # Discard the right half and narrow our search to the left half.
                    right = mid - 1

        # If the loop finishes without finding the target (i.e., 'left' crosses 'right'),
        # it means the target is not present in the array.
        # As the problem asks for a boolean result, we return False.
        return False