class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        

        def bisectLeft(target):

            left, right= 0, len(nums) - 1
            
            while left <= right:

                mid = (left + right) // 2
                num = nums[mid]

                if num < target:

                    left = mid + 1
                
                elif num > target:

                    right = mid - 1
                
                else:

                    return mid
                
            return left
        

        return bisectLeft(target)