class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        n = len(blocks)
        l = 0
        cur_win = 0
        max_win = 0

        for i in range(k):

            if blocks[i] == 'B':

                cur_win += 1
        

        max_win = max(max_win, cur_win)

        for r in range(k, n):

            if blocks[r] == 'B':

                cur_win += 1
            
            if blocks[l] == 'B':

                cur_win -= 1
            
            l += 1

            max_win = max(max_win, cur_win)


        return k - max_win