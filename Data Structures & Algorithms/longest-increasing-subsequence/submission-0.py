class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        tab = [1] * n

        for i in reversed(range(n)):
            for j in range(i, n):

                if nums[j] > nums[i]:

                    tab[i] = max(tab[i], 1 + tab[j])
        
        print(tab)
        return max(tab)