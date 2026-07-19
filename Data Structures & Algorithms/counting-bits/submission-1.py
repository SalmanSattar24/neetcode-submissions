class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count_ones(num):

            bitmask = 1 << 0
            ones = 0

            for i in range(32):

                ones += num & bitmask
                num = num >> 1
            
            return ones
        

        res = []

        for i in range(n + 1):

            ones = count_ones(i)
            res.append(ones)
        
        return res