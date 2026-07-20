class Solution:
    def reverse(self, x: int) -> int:
        
        MAX, MIN = ((2 ** 31) - 1), -2 ** 31
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:

            last_digit = x % 10
            x = x // 10

            if (
                res > MAX // 10 or
                res == MAX // 10 and last_digit > MAX % 10
            ):
                return 0
            

            res = (res * 10) + last_digit
        
        return res * sign