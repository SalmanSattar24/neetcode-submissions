class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        n = len(nums)
        res = []
        i = 0

        while i < n - 1 - 1:

            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            k = n - 1

            while j < k:

                summ = nums[i] + nums[j] + nums[k]

                if summ == 0:

                    res.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                
                elif summ < 0:
                    j += 1
                
                elif summ > 0:
                    k -= 1

            i += 1

        return res