class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize two pointers:
        # 'left' tracks the position where valid elements should be placed
        # 'right' starts at the end of the array and moves left when removing elements
        left, right = 0, len(nums)

        # Loop until the left pointer reaches the right boundary
        while left < right:
            # If the current element matches 'val', we need to remove it
            if nums[left] == val:
                # Reduce the right boundary since we're removing an element
                right -= 1

                # Swap the current element with the last valid element in the range
                # This ensures that elements equal to 'val' are pushed out of the valid range
                nums[left] = nums[right]
            else:
                # If the current element is valid, move the left pointer forward
                left += 1

        # The final value of 'left' represents the count of remaining valid elements
        return left
