class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        N = len(s)
        longest_palindrome = 0
        start_index = 0

        for i in range(N):

            left, right = i, i

            while left >= 0 and right < N and s[left] == s[right]:
                
                if right - left + 1 > longest_palindrome:

                    longest_palindrome = right - left + 1
                    start_index = left
                    
                left -= 1
                right += 1
            
            left, right = i, i + 1

            while left >= 0 and right < N and s[left] == s[right]:
                
                if right - left + 1 > longest_palindrome:

                    longest_palindrome = right - left + 1
                    start_index = left

                left -= 1
                right += 1
            
        
        return s[start_index : start_index + longest_palindrome]