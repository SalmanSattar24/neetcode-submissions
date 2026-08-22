class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        l = 0
        n = len(nums)
        arr_sum = 0
        max_win = 1

        for r in range(n):

            arr_sum += nums[r]

            while (r - l + 1) * nums[r] - arr_sum > k:

                arr_sum -= nums[l]
                l += 1

            max_win = max(max_win, r - l + 1)
        

        return max_win