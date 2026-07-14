class Solution:
    def rob(self, nums: List[int]) -> int:
        
        N = len(nums)
        if N <= 2:
            return max(nums)


        # memo = {}

        # def rob_house(nums, house):

        #     if house >= N:
        #         return 0
            
        #     if house in memo:
        #         return memo[house]
            
        #     memo[house] = max(nums[house] + rob_house(house + 2), rob_house(house + 1))

        #     return memo[house]

        # return max(rob_house(0), rob_house(1))


        def rob_house(nums):

            tab = {}

            for house in reversed(range(len(nums))):

                tab[house] = max(nums[house] + tab.get(house + 2, 0), tab.get(house + 1, 0))
            
            return max(tab[0], tab[1])
        
        return max(rob_house(nums[1:]), rob_house(nums[: -1]))
        
