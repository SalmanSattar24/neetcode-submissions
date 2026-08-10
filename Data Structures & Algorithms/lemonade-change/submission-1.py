class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five, ten = 0, 0

        for b in bills:

            if b == 5:
                five += 1
            
            elif b == 10:
                if five > 0:
                    ten += 1
                    five -= 1
                else:
                    return False
            
            else:
                if five > 0:
                    if ten > 0:
                        five -= 1
                        ten -= 1
                    elif five >= 3:
                        five -= 3
                    else:
                        return False
                
                else:
                    return False
        
        return True