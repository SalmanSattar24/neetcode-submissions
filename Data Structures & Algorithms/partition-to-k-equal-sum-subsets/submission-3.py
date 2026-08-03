class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k != 0:
            return False
        
        nums.sort(reverse=True)
        partitions = [0] * k
        max_size = sum(nums) // k

        def backtrack(i):

            if i >= len(nums):
                # return equal_subsets(partitions)
                return True
            
            for p in range(k):

                if partitions[p] + nums[i] <= max_size:

                    partitions[p] += nums[i]
                    
                    if backtrack(i + 1):
                        return True
                    
                    partitions[p] -= nums[i]
                    
                    if partitions[p] == 0:
                        break

            return False
        
        # def equal_subsets(subsets):

        #     for i in range(1, len(subsets)):

        #         if subsets[i] != subsets[i - 1]:
        #             return False
            
        #     return True
        
        
        return backtrack(0)
        