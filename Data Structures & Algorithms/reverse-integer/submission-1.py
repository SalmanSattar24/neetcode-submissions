class Solution:
    def reverse(self, x: int) -> int:
        
        MAX, MIN = ((2 ** 31) - 1), -2 ** 31
        res = 0

        while x:

            last_digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (
                abs(res) > MAX // 10 or
                abs(res) == MAX // 10 and last_digit > MAX % 10
            ):
                return 0
            
            # if (

            # )

            res = (res * 10) + last_digit
        
        return res