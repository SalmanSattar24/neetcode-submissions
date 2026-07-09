class Solution:
    def mySqrt(self, x: int) -> int:
        # Edge case: square root of 0 or 1 is itself
        if x < 2:
            return x

        # Initialize binary search bounds
        # √x lies between 1 and x//2 for x >= 2
        left, right = 0, x // 2

        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid

            if squared < x:
                # Midpoint squared is too small, try higher values
                left = mid + 1
            elif squared > x:
                # Midpoint squared is too large, try lower values
                right = mid - 1
            else:
                # Found exact square root
                return mid

        # Loop ended without exact match: return the floor of √x
        # 'right' holds the largest mid where mid² <= x
        return right
