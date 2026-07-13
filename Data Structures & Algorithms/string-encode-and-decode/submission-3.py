class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            # Wrap each string in brackets to act as boundaries
            encoded.append('(')
            encoded.append(s)
            encoded.append(')')
            
        # Combine everything into a single flattened string
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        stack = collections.deque()
        result = []
        start = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Track opening bracket to handle nested/inner brackets safely
                stack.append('(')
            elif char == ')':
                stack.pop()
                
                # If the stack is empty, we found the matching outer bracket
                if not stack:
                    # Slice the original string between the outer brackets
                    result.append(s[start + 1 : i])
                    # Move the start pointer right past the current closing bracket
                    start = i + 1
                    
        return result