class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo =  defaultdict(int)
        memo[target] = 1

        for t in reversed(range(target + 1)):
            for num in nums:

                if t == target:
                    continue

                memo[t] += memo.get(t + num, 0)
        
        return memo[0]
        
