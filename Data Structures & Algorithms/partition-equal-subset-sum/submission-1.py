class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        summ = sum(nums)
        t = summ // 2

        if summ % 2 != 0:
            return False
        
        n = len(nums)
        memo = {}
        for j in range(n + 1):
            memo[(j, 0)] = True


        for i in reversed(range(n - 1)):
            for j in range(t + 1):

                take = memo.get((i + 1, j - nums[i]), False)
                skip = memo.get((i + 1, j), False)

                memo[(i, j)] = take or skip

        return memo[(0, t)]
        