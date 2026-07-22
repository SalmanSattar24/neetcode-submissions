class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        continous_max, continous_min = nums[0], nums[0]
        current_max, current_min = 0, 0

        for num in nums:

            current_max = max(current_max + num, num)
            continous_max = max(continous_max, current_max)

            current_min = min(current_min + num, num)
            continous_min = min(continous_min, current_min)
        
        total = sum(nums)

        if continous_max < 0:
            return continous_max
            
        return max(continous_max, total - continous_min)