class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        nums.sort()
        l, r = 0, k - 1
        diff = nums[k - 1] - nums[0]

        while r < n:

            diff = min(diff, nums[r] - nums[l])

            r += 1
            l += 1
        
        return diff