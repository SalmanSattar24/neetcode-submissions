class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        N = len(cost)
        memo = {}

        def calculate_cost(step):
            
            if step >= N:
                return 0
            
            if step in memo:
                return memo[step]

            memo[step] = cost[step] + min(calculate_cost(step + 1), calculate_cost(step + 2))

            return memo[step]
        
        return min(calculate_cost(1), calculate_cost(0))