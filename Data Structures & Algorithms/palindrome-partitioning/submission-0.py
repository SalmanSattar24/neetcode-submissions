class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        partition = []

        def backtrack(i):

            if i >= len(s):
                result.append(partition.copy())
                return
            
            for j in range(i, len(s)):

                if is_palindrome(i, j):
                    
                    partition.append(s[i : j + 1])
                    backtrack(j + 1)
                    partition.pop()


        def is_palindrome(i, j):

            while i < j:

                if s[i] != s[j]:
                    return False
                
                i += 1
                j -= 1

            return True
        
        backtrack(0)
        return result