class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        global_max = nums[0]
        current_max = 0

        for num in nums:

            current_max = max(current_max + num, num)
            global_max = max(global_max, current_max)
        
        return global_max
        