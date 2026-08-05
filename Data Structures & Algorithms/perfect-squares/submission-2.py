class Solution:
    def numSquares(self, n: int) -> int:
        
        memo = {0 : 0}   
        
        for t in range(1, n + 1):
            
            # worst case is to just use only 1s 
            min_squares = t
            
            for i in range(1, t + 1):
                
                if i * i > t:
                    break


                min_squares = (
                    min(
                        min_squares,
                        1 + memo.get(t - i * i)
                    )
                )

                memo[t] = min_squares

        return memo[n]