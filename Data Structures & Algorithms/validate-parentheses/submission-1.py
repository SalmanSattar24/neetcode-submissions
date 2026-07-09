class Solution:
    def isValid(self, s: str) -> bool:
        # Define a dictionary to store the mapping of closing parentheses to their corresponding opening parentheses
        parentheses = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Initialize an empty list to act as a stack
        stack = []
        
        # Iterate through each character in the input string 's'
        for char in s:
            # If the current character is an opening parenthesis, push it onto the stack
            if char in parentheses.values():
                stack.append(char)
            # If the current character is a closing parenthesis
            elif char in parentheses.keys():
                # If the stack is empty, it means there's no matching opening parenthesis, so it's invalid
                if not stack:
                    return False
                # If the top of the stack does not match the corresponding opening parenthesis for the current closing parenthesis, it's invalid
                elif stack.pop() != parentheses[char]:
                    return False
            # If the character is not a parenthesis, it's an invalid character (though problem constraints usually guarantee only parentheses)
            else:
                return False # Or handle as per problem's specific requirements for invalid characters

        # After iterating through all characters, if the stack is empty, all parentheses were matched
        # Otherwise, there are unmatched opening parentheses, so it's invalid
        return not stack