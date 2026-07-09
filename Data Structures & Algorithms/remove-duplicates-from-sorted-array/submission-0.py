class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left, n = 0, len(nums)

        for right in range(1, n):

            if nums[left] == nums[right]:
                continue
            
            left += 1
            nums[left] = nums[right]
        
        print(nums)

        return left + 1