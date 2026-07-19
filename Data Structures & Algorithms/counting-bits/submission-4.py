class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            
            msb_val = 1 << (i.bit_length() - 1)
            
            dp[i] = 1 + dp[i - msb_val]

        return dp