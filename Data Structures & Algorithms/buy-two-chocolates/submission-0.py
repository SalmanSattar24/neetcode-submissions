class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        min1 = min2 = math.inf

        for p in prices:

            if p < min1:

                min2 = min1
                min1 = p
            
            elif p < min2:

                min2 = p
        
        leftover = money - (min1 + min2) 

        return leftover if leftover >= 0 else money