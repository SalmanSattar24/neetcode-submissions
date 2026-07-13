class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = []

        for s in strs:

            encoded.append('(')
            encoded.append(s)
            encoded.append(')')

        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:

        stack = collections.deque()
        result = []
        start = 0

        for i, char in enumerate(s):

            if char == '(':
                stack.append('(')
            
            elif char == ')':
                stack.pop()

                if not stack:
                    result.append(s[start + 1: i])
                    start = i + 1
        
        return result