class Solution:
    def numDecodings(self, s: str) -> int:
        
        N = len(s)
        
        
        memo = {}

        def recurse(index):

            if index >= N:
                return 1

            if s[index] == '0':
                return 0
            
            if index in memo:
                return memo[index]
            
            take_one = recurse(index + 1)

            take_two = 0
            if index + 1 < N and int(s[index : index + 2]) <= 26:
                take_two = recurse(index + 2)

            memo[index] = take_one + take_two

            return memo[index]
        
        # return recurse(0)
    

        tab = {}

        for index in reversed(range(N)):

            if s[index] == '0':
                tab[index] = 0
                continue
            
            take_one = tab.get(index + 1, 1)

            take_two = 0
            if index + 1 < N and int(s[index : index + 2]) <= 26:
                take_two = tab.get(index + 2, 1)
            
            tab[index] = take_one + take_two

        return tab[0]
