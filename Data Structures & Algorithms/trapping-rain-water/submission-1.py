class Solution:
    def trap(self, height: List[int]) -> int:
        # Initialize two pointers: 'left_wall_idx' at the start and 'right_wall_idx' at the end of the height array.
        left_wall_idx, right_wall_idx = 0, len(height) - 1

        # Initialize 'max_height_from_left' and 'max_height_from_right'
        # with the heights of the initial bars at the pointers.
        max_height_from_left = height[left_wall_idx]
        max_height_from_right = height[right_wall_idx]

        # Initialize 'total_trapped_water' to accumulate the water.
        total_trapped_water = 0

        # Loop as long as the left pointer is to the left of the right pointer.
        # This ensures there's a valid width between the two "walls".
        while left_wall_idx < right_wall_idx:
            # Decide which pointer to move based on which side has the smaller current max height.
            # Water trapping is limited by the shorter of the two bounding walls.
            if max_height_from_left < max_height_from_right:
                # If the left maximum is smaller, focus on the left side.
                left_wall_idx += 1  # Move the left pointer one step to the right.

                # If the new bar is taller than the current 'max_height_from_left', update the max.
                if height[left_wall_idx] >= max_height_from_left:
                    max_height_from_left = height[left_wall_idx]
                # Otherwise (if the new bar is shorter), water can potentially be trapped.
                else:
                    # Add water trapped at this position: (limiting wall height - current bar height).
                    total_trapped_water += max_height_from_left - height[left_wall_idx]

            else:
                # If the right maximum is smaller or equal, focus on the right side.
                right_wall_idx -= 1  # Move the right pointer one step to the left.

                # If the new bar is taller than the current 'max_height_from_right', update the max.
                if height[right_wall_idx] >= max_height_from_right:
                    max_height_from_right = height[right_wall_idx]
                # Otherwise (if the new bar is shorter), water can potentially be trapped.
                else:
                    # Add water trapped at this position: (limiting wall height - current bar height).
                    total_trapped_water += max_height_from_right - height[right_wall_idx]

        # Return the total calculated trapped water.
        return total_trapped_water