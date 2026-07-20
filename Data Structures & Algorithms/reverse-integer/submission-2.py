class Solution:
    def reverse(self, x: int) -> int:
        
        MAX, MIN = ((2 ** 31) - 1), -2 ** 31
        res = 0

        while x:

            last_digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (
                res > MAX // 10 or
                res == MAX // 10 and last_digit > MAX % 10
            ):
                return 0
            
            if (
                res < MIN // 10 or 
                res == MIN // 10 and last_digit < MIN % 10
            ):
                return 0

            res = (res * 10) + last_digit
        
        return res