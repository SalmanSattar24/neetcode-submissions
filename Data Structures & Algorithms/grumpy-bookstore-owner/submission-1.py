class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        n = len(customers)
        
        base_satisfied = 0
        for i in range(n):
            
            if grumpy[i] == 0:
                base_satisfied += customers[i]
        

        bonus_satisfied = 0
        for j in range(minutes):

            if grumpy[j] == 1:
                bonus_satisfied += customers[j]
        

        max_bonus_satisfied = bonus_satisfied
        for r in range(minutes, n):

            l = r - minutes

            if grumpy[l] == 1:
                bonus_satisfied -= customers[l]
            
            if grumpy[r] == 1:
                bonus_satisfied += customers[r]
            
            max_bonus_satisfied = max(max_bonus_satisfied, bonus_satisfied)

        
        return max_bonus_satisfied + base_satisfied