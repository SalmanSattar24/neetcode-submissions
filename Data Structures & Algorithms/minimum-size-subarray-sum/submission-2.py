class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        current_sum = 0
        left = 0
        min_subarray_len = float('inf')

        for right in range(len(nums)):

            current_sum += nums[right]

            while current_sum >= target and left <= right:

                min_subarray_len = min(min_subarray_len, right - left + 1)
                
                current_sum -= nums[left]
                left += 1

        
        
        return 0 if min_subarray_len == float('inf') else min_subarray_len