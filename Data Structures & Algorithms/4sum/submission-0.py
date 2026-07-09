class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        quad = []
        res = []
        nums.sort()

        def kSum(k, start, target):

            if k == 2:

                left, right = start, len(nums) - 1

                while left < right:

                    summ = nums[left] + nums[right]

                    if summ < target:
                        left += 1
                    
                    elif summ > target:
                        right -= 1
                    
                    else:
                        res.append(quad + [nums[left], nums[right]])

                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                
                return
                
            
            for i in range(start, len(nums) - k + 1):

                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()
            
        kSum(4, 0, target)
        return res