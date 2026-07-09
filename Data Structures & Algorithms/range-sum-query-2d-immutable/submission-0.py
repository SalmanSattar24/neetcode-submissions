from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        """
        Initializes the NumMatrix object with a given 2D matrix.
        Uses a prefix sum approach to preprocess the matrix for efficient range sum queries.

        :param matrix: 2D list of integers representing the matrix.
        """
        if not matrix or not matrix[0]:  # Handle edge case where matrix is empty
            return
        
        # Get the number of rows and columns in the matrix
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])

        # Create a prefix sum matrix (dp) with an extra row and column for easier calculations
        # dp[i][j] represents the sum of elements in the submatrix from (0,0) to (i-1,j-1)
        self.dp = [[0] * (self.COLS + 1) for _ in range(self.ROWS + 1)]

        # Populate the prefix sum matrix using the inclusion-exclusion principle
        for row in range(self.ROWS):
            for col in range(self.COLS):
                # Sum of elements above the current row
                rect_above_this_row = self.dp[row + 1][col]
                
                # Sum of elements to the left of the current column
                rect_behind_this_col = self.dp[row][col + 1]
                
                # Value of the current cell in the original matrix
                val_of_current_cell = matrix[row][col]
                
                # Overlapping region that was counted twice (needs to be subtracted)
                overlap_region = self.dp[row][col]

                # Compute the prefix sum for the current cell using the formula:
                # dp[r+1][c+1] = dp[r+1][c] + dp[r][c+1] + matrix[r][c] - dp[r][c]
                self.dp[row + 1][col + 1] = rect_above_this_row + rect_behind_this_col + val_of_current_cell - overlap_region

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Returns the sum of elements in the submatrix defined by (row1, col1) to (row2, col2).
        Uses the precomputed prefix sum matrix to compute the sum in O(1) time.

        :param row1: Top-left row index of the submatrix.
        :param col1: Top-left column index of the submatrix.
        :param row2: Bottom-right row index of the submatrix.
        :param col2: Bottom-right column index of the submatrix.
        :return: Sum of elements in the specified submatrix.
        """
        # Inclusion-exclusion principle to compute the sum efficiently:
        # Sum of the entire region from (0,0) to (row2,col2)
        origin_to_bottom_right = self.dp[row2 + 1][col2 + 1]
        
        # Subtract the area above the selected submatrix
        area_above = self.dp[row1][col2 + 1]
        
        # Subtract the area to the left of the selected submatrix
        area_left = self.dp[row2 + 1][col1]
        
        # Add back the overlapping region that was subtracted twice
        overlap_region = self.dp[row1][col1]

        # Compute the final sum using the formula:
        # sumRegion = dp[row2+1][col2+1] - dp[row1][col2+1] - dp[row2+1][col1] + dp[row1][col1]
        return origin_to_bottom_right - area_above - area_left + overlap_region



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)