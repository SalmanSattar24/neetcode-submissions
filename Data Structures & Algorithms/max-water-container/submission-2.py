class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Calculates the maximum amount of water that can be contained
        between two vertical lines in the 'heights' array.

        This problem is solved using the two-pointer technique for optimal
        time complexity.
        """

        # Initialize `max_water_contained` to store the largest area found so far.
        # We start with 0 as no area has been calculated yet.
        max_water_contained = 0

        # Initialize two pointers:
        # `left_ptr` at the beginning of the array.
        # `right_ptr` at the end of the array.
        left_ptr = 0
        right_ptr = len(heights) - 1

        # Continue the loop as long as the left pointer is to the left of the right pointer.
        # This ensures we always have a valid width for a container.
        while left_ptr < right_ptr:
            # Calculate the height of the current container.
            # The water level is limited by the shorter of the two lines.
            current_height = min(heights[left_ptr], heights[right_ptr])

            # Calculate the width of the current container.
            # This is simply the distance between the two pointers.
            current_width = right_ptr - left_ptr

            # Calculate the area of the current container.
            current_area = current_height * current_width

            # Update `max_water_contained` if the current area is greater.
            max_water_contained = max(max_water_contained, current_area)

            # Move the pointer that points to the shorter line inward.
            # The intuition here is that moving the taller line inward will
            # always result in a smaller or equal height (because the shorter
            # line remains the limiting factor) and a smaller width.
            # Moving the shorter line, however, might allow us to find a taller
            # line that could create a larger container.
            if heights[left_ptr] < heights[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        # Once the pointers meet or cross, all possible valid containers have been checked.
        # Return the maximum area found.
        return max_water_contained