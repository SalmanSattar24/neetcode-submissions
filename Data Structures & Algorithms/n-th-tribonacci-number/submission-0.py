class Solution:
    def tribonacci(self, n: int) -> int:
        
        tab = {0: 0, 1: 1, 2: 1}

        for i in range(3, n + 1):

            tab[i] = tab.get(i - 1, 0) + tab.get(i - 2, 0) + tab.get(i - 3, 0)
        
        return tab.get(n)