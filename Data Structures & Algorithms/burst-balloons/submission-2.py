class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]
        memo = defaultdict(int)

        def recurse(l, r):

            if l > r:
                return 0
            
            key = (l, r)
            if key in memo:
                return memo[key]
            

            for i in range(l, r + 1):

                coins = nums[l - 1] * nums[i] * nums[r + 1]

                coins += recurse(l, i - 1) + recurse(i + 1, r)

                memo[key] = max(memo[key], coins)

            return memo[key]
        

        return recurse(1, len(nums) - 2)