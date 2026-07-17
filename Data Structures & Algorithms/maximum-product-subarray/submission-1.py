class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        current_min, current_max = 1, 1

        for num in nums:

            if num == 0:
                current_min, current_max = 1, 1
                continue
            
            temp_current_max = current_max
            current_max = max(current_max * num, current_min * num, num)
            current_min = min(temp_current_max * num, current_min * num, num)

            res = max(res, current_max)
        
        return res