class Solution:
    def totalNQueens(self, n: int) -> int:
        
        cols = set()
        pos_diag = set()
        neg_diag = set()
        results = 0

        def backtrack(r):

            nonlocal results

            if r == n:
                results += 1
                return
            
            
            for c in range(n):

                if (
                    c not in cols and 
                    r + c not in pos_diag and 
                    r - c not in neg_diag 
                ):

                    cols.add(c)
                    pos_diag.add(r + c)
                    neg_diag.add(r - c)

                    backtrack(r + 1)

                    cols.remove(c)
                    pos_diag.remove(r + c)
                    neg_diag.remove(r - c)
        
        backtrack(0)
        return results