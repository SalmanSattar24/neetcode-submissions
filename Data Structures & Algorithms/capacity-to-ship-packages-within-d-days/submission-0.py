class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def daysNeeded(capacity):

            reamining_capacity = capacity
            num_days = 1

            for weight in weights:

                if reamining_capacity >= weight:
                    reamining_capacity -= weight

                else:
                    num_days += 1
                    reamining_capacity = capacity
                    reamining_capacity -= weight
            
            return num_days

        min_capacity, max_capacity = max(weights), sum(weights)
        res = 1

        while min_capacity <= max_capacity:

            new_capacity = (min_capacity + max_capacity) // 2
            days_needed_to_ship = daysNeeded(new_capacity)

            if days_needed_to_ship > days:
                min_capacity = new_capacity + 1
            
            else:
                res = new_capacity
                max_capacity = new_capacity - 1
        
        return res