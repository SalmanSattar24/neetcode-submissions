class Solution:
    def rob(self, nums: List[int]) -> int:
        
        N = len(nums)
        memo = {}

        def rob_house(house):

            if house >= N:
                return 0
            
            if house in memo:
                return memo[house]
            
            memo[house] = max(nums[house] + rob_house(house + 2), rob_house(house + 1))

            return memo[house]

        return max(rob_house(0), rob_house(1))