class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        left, right = 0, len(s) - 1
        
        def validAlphsNum(char):

            if(
                48 <= ord(char) <= 57 or
                97 <= ord(char) <= 122
            ):
                return True
            
            else:
                return False

        while left < right:

            if validAlphsNum(s[left]) == False:
                
                left += 1
                continue
            
            if validAlphsNum(s[right]) == False:

                right -= 1
                continue

            if s[left] != s[right]:
                
                return False
            
            left +=1
            right -= 1
        
        return True