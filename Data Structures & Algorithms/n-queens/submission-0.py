class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = set()
        pos_diag = set()
        neg_diag = set()
        result = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(r):

            if r == n:
                copy = [''.join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):

                if (
                    r + c in pos_diag or
                    r - c in neg_diag or
                    c in cols
                ):
                    continue
                
                board[r][c] = 'Q'
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                cols.add(c)

                backtrack(r + 1)

                board[r][c] = '.'
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                cols.remove(c)
        

        backtrack(0)
        return result