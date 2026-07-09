class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_rate, max_rate = 1, max(piles)
        k = max_rate

        def eatingTime(rate):
            
            time = 0

            for pile in piles:

                time += math.ceil(float(pile) / rate)
            
            return time

        while min_rate <= max_rate:

            new_rate = (min_rate + max_rate) // 2
            time_needed = eatingTime(new_rate)

            if time_needed > h:
                min_rate = new_rate + 1
            
            else:
                k = new_rate
                max_rate = new_rate - 1
        
        return k