class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Time Complexity: O(n)
        # Each element is pushed onto and popped from the stack at most once.
        # The loop runs 'n' times, and stack operations (append, pop, peek) are O(1).

        # Space Complexity: O(n)
        # In the worst case (e.g., a strictly increasing histogram), the stack can store
        # all 'n' elements.

        # Initialize a stack to store (height, index) tuples.
        # The stack will maintain a monotonically increasing sequence of heights.
        # We start with a sentinel (0, -1). This acts as a dummy bar of height 0
        # at an index before the actual histogram begins. It's crucial for correctly
        # calculating the width of rectangles that extend all the way to the left
        # and prevents IndexError when the stack might otherwise become empty.
        stack = [(0, -1)]

        # Initialize max_area to 0, which will store the largest rectangle area found so far.
        max_area = 0

        # Append a 0 to the heights array. This is a critical step.
        # This trailing '0' acts as a sentinel to ensure that all remaining bars
        # in the stack (which are in increasing order of height) are processed
        # and their potential areas are calculated when the loop finishes.
        # It forces all bars to be "popped" and evaluated.
        heights.append(0)

        # Iterate through the (modified) heights array using enumerate to get both
        # the index (i) and the height of the current bar.
        for i, height in enumerate(heights):
            # This 'while' loop is the core of the monotonic stack logic.
            # It continues as long as the stack is not effectively empty (i.e., has more than just the sentinel)
            # and the height of the bar at the top of the stack is GREATER than the current bar's height.
            # We use '>' instead of '>=' to ensure that if we encounter a bar of the same height,
            # we push it and potentially extend the width of the rectangle based on the earlier, same-height bar's index.
            # This helps in finding the widest possible rectangle for a given height.
            while stack[-1][0] > height:
                # If the condition is met, it means we've found a bar (current 'height')
                # that is smaller than the bar at the top of our stack (prev_height).
                # This 'current_height' now acts as the "right smaller element" for 'prev_height'.
                # Pop the (prev_height, prev_index) tuple from the stack.
                prev_height, prev_index = stack.pop()

                # Calculate the 'left_limit' for the rectangle formed by 'prev_height'.
                # The 'left_limit' is the index of the bar that is just to the left
                # of 'prev_height' and is *smaller* than 'prev_height'.
                # This bar is now at the top of the stack *after* 'prev_height' has been popped.
                # If the stack only contains the initial sentinel (0, -1), then stack[-1][1] will be -1.
                left_limit = stack[-1][1]

                # The 'right_limit' for 'prev_height' is the current index 'i'.
                # This is because 'heights[i]' is the first bar to the right that is smaller than 'prev_height'.
                right_limit = i

                # Calculate the width of the rectangle formed by 'prev_height'.
                # The width is (right_limit - left_limit - 1).
                # - 'right_limit' is the exclusive right boundary (index of the first smaller bar to the right).
                # - 'left_limit' is the exclusive left boundary (index of the first smaller bar to the left).
                # - Subtracting 1 converts from exclusive indices to the actual count of bars.
                # Example: if right_limit = 5, left_limit = 1, width = 5 - 1 - 1 = 3 (bars at indices 2, 3, 4).
                width = right_limit - left_limit - 1

                # Calculate the area of this rectangle.
                area = prev_height * width

                # Update max_area if the current rectangle's area is larger.
                max_area = max(max_area, area)

            # After processing all bars taller than or equal to the current 'height',
            # push the current (height, index) onto the stack.
            # This maintains the monotonic increasing property of the stack (by height).
            stack.append((height, i))

        # After the loop completes (all bars, including the appended 0, have been processed),
        # max_area will hold the largest rectangle area.
        return max_area