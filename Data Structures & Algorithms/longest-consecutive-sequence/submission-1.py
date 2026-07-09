class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        num_set = set(nums)
        lcs = 1

        for num in nums:

            if (num - 1) not in num_set:

                new_length = 0

                while num + new_length in num_set:
                    
                    
                    new_length += 1
                
                lcs = max(lcs, new_length)
        
        return lcs
                