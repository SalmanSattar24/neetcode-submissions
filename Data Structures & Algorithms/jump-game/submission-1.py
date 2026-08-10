class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_steps = 0

        for i, n in enumerate(nums):

            if i > max_steps:
                return False

            if i + n > max_steps:
                max_steps = i + n
        
        return max_steps >= len(nums) - 1