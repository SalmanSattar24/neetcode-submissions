class Solution:
    def isValid(self, s: str) -> bool:
        
        parentheses = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for char in s:

            if not stack:
                stack.append(char)
            
            elif char in parentheses and parentheses[char] == stack[-1]:
                stack.pop()
            
            else:
                stack.append(char)
            
        if not stack:
            return True
        
        return False