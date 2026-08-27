''' Ineffient Solution'''

import sys
sys.setrecursionlimit(20000)

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        memo = {}

        def recurse(l, r, s):
            if r == n or s > goal:
                return 0

            key = (l, r, s)
            if key in memo:
                return memo[key]

            new_sum = s + nums[r]
            res = 0

            # Option 2: Explore new subarray start at l + 1 BEFORE pruning current path
            if l == r:
                res += recurse(l + 1, l + 1, 0)

            # Prune current expansion path if sum exceeds target goal
            if new_sum > goal:
                memo[key] = res
                return res

            count = 1 if new_sum == goal else 0

            # Option 1: Continue expanding rightward
            res += count + recurse(l, r + 1, new_sum)

            memo[key] = res
            return res

        return recurse(0, 0, 0)