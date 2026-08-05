class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        summ = sum(nums)
        half = summ // 2

        if summ % 2 != 0:
            return False
        
        n = len(nums)
        memo = {}
        for i in range(n):
            memo[(i, half)] = True


        for i in reversed(range(n - 1)):
            for j in reversed(range(half + 1)):

                take = memo.get((i + 1, j + nums[i]), False)
                skip = memo.get((i + 1, j), False)

                memo[(i, j)] = take or skip

        return memo[(0, 0)]
        