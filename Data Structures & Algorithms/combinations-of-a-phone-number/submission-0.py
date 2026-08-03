class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []
        
        result, combo = [], []
        digits_to_char = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        def backtrack(i):

            if len(combo) == len(digits):
                result.append(''.join(combo))
                return
            
            for char in digits_to_char[digits[i]]:

                combo.append(char)
                backtrack(i + 1)

                combo.pop()
        
        backtrack(0)
        return result