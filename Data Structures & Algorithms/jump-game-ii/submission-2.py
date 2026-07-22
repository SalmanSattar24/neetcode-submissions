class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        left = right = 0

        while right < len(nums) - 1:

            farthest_jump = 0

            for i in range(left, right + 1):

                farthest_jump = max(farthest_jump, i + nums[i])
            
            left = right
            right = farthest_jump
            jumps += 1
        
        return jumps