class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        n = len(fruits)
        count = Counter()
        l = 0
        max_win = 0

        for r in range(n):

            count[fruits[r]] += 1

            while len(count) > 2:
                
                count[fruits[l]] -= 1

                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                
                l += 1

            max_win = max(max_win, r - l + 1)
        

        return max_win