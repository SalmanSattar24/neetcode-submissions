class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2
            mid_num = nums[mid]

            if mid_num < nums[right]:
                right = mid
            
            else:
                left = mid + 1
        
        return mid_num
        
