class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # ---------------------------------------------------------------
        # Time Complexity:  O(log(ROWS * COLS))
        #   → Binary search on a virtually flattened matrix.
        #
        # Space Complexity: O(1)
        #   → No additional data structures used; operates in-place.
        # ---------------------------------------------------------------

        # Calculate the number of rows and columns in the matrix
        ROWS, COLS = len(matrix), len(matrix[0])  # Used to translate 1D indices to 2D positions

        # Set binary search pointers for the virtual flat matrix
        left, right = 0, ROWS * COLS - 1  # Think of this as a 1D list of all matrix elements

        # Begin standard binary search loop
        while left <= right:

            # Midpoint index in the virtual 1D array
            mid = (left + right) // 2  # Prevents overflow with integer division

            # --- Convert `mid` to 2D coordinates in the matrix ---
            # Row index is total number of complete rows within `mid`
            row = mid // COLS  # e.g. mid=5, COLS=4 → row=1 (second row)

            # Column index is remainder when `mid` is divided by COLS
            col = mid % COLS   # e.g. mid=5, COLS=4 → col=1 (second column)
            # This breakdown isolates the matrix element corresponding to index `mid`

            # Retrieve the actual value from the matrix at computed (row, col)
            val = matrix[row][col]

            # Decision point: move search boundaries based on comparison
            if val < target:
                left = mid + 1  # Target lies in the right half
            elif val > target:
                right = mid - 1  # Target lies in the left half
            else:
                return True  # Found the target element

        # Target not present after exhausting search range
        return False
