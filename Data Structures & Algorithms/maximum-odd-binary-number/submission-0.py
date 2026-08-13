class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        res = deque()

        for char in s:

            if char =='1':

                res.append(char)
            
            else:

                res.appendleft(char)
        
        print(res)
        
        left, right = 0, len(s) - 2

        while left < right:

            res[left], res[right] = res[right], res[left]
            
            left += 1
            right -= 1
        
        print(res)
        
        return ''.join(res)