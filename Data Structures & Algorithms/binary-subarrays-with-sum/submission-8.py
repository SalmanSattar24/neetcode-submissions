class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        n = len(nums)

        def subarrays_at_most_k(k):

            if k < 0:
                return 0

            win_sum = 0
            l = 0
            res = 0

            for r in range(n):

                win_sum += nums[r]

                while win_sum > k:

                    win_sum -= nums[l]
                    l += 1
                
                res += r - l + 1
            
            return res
        
        return subarrays_at_most_k(goal) - subarrays_at_most_k(goal - 1)