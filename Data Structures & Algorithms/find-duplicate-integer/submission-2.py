class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for num in nums:

            key = abs(num) - 1

            if nums[key] < 0:
                return abs(num)
            
            nums[key] *= -1