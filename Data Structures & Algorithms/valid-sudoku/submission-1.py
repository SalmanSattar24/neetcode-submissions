from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determines if a 9x9 Sudoku board is valid.
        - Each row, column, and 3x3 sub-box must contain unique digits (1-9).
        - Empty cells (".") are ignored.
        
        Approach:
        - Use sets to track seen numbers in rows, columns, and sub-boxes.
        - Iterate through the board and check for duplicates before adding numbers to sets.
        
        Complexity:
        - Time Complexity: O(81) ≈ O(1), since the board size is fixed.
        - Space Complexity: O(81) ≈ O(1), due to storing numbers in sets.
        """

        # Initialize sets for rows, columns, and sub-boxes
        row_set = [set() for _ in range(9)]  # Tracks numbers in each row
        col_set = [set() for _ in range(9)]  # Tracks numbers in each column
        box_set = {(i, j): set() for i in range(3) for j in range(3)}  # Tracks numbers in each 3x3 sub-box

        # Iterate through the board
        for r in range(9):  # Loop through rows
            for c in range(9):  # Loop through columns
                num = board[r][c]  # Get the current cell value
                
                if num == ".":  # Skip empty cells
                    continue
                
                # Calculate the correct box index using (r // 3, c // 3)
                box_index = (r // 3, c // 3)

                # Check for duplicates in row, column, or sub-box
                if(
                    num in row_set[r] or
                    num in col_set[c] or
                    num in box_set[box_index]
                ):
                    return False  # If duplicate found, board is invalid
                
                # Add number to respective sets
                row_set[r].add(num)  # Add to row tracking set
                col_set[c].add(num)  # Add to column tracking set
                box_set[box_index].add(num)  # Add to sub-box tracking set

        return True  # If no duplicates found, board is valid
