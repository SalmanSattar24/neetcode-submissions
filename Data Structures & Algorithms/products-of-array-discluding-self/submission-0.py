from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Computes the product of all elements except self for each index in nums.
        Uses prefix and postfix multipliers to achieve O(n) time complexity with O(1) extra space.
        """

        L = len(nums)  # Get the length of the input array
        
        res = [1] * L  # Initialize result array with 1s
        
        prefix = 1  # Tracks cumulative product from the left
        
        # First pass: Compute prefix products
        for i in range(L):
            res[i] = prefix  # Store the prefix product at index i
            prefix *= nums[i]  # Update prefix for the next index
        
        postfix = 1  # Tracks cumulative product from the right
        
        # Second pass: Compute postfix products and multiply with prefix values
        for j in reversed(range(L)):  # Iterate from right to left
            res[j] *= postfix  # Multiply current result by postfix product
            postfix *= nums[j]  # Update postfix for the next index
        
        return res  # Return the final computed array
