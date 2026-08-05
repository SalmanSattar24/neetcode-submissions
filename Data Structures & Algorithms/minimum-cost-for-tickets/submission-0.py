class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        days_set = set(days)
        memo = {0 : 0}

        for i in range(1, max(days) + 1):

            if i not in days_set:
                memo[i] = memo[i - 1]
                continue
            
            memo[i] = math.inf

            for d, c in zip([1, 7, 30], costs):

                memo[i] = min(
                    memo.get(i), 
                    memo.get(i - d, 0) + c
                )
        
        return memo[max(days)]