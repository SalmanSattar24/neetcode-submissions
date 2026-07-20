class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        
        for i in range(32):

            temp = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = temp
        
        return a if a <= max_int else ~(a ^ mask)
