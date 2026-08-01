class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        parens = []
        
        def backtrack(o, c):

            if o + c == 2 * n:
                result.append(''.join(parens))
                return
            
            if o < n:
                
                parens.append('(')
                backtrack(o + 1, c)

                parens.pop()

            if o > c:

                parens.append(')')
                backtrack(o, c + 1)

                parens.pop()

        backtrack(0, 0)
        return result