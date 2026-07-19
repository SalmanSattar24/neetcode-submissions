class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0

        bitmask = 1 << 0
        
        for i in range(32):

            res += bitmask & n
            n = n >> 1

        return res