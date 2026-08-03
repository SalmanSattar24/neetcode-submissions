class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        if sum(matchsticks) % 4 != 0:
            return False
        
        matchsticks.sort(reverse=True)
        sides = [0, 0, 0, 0]
        single_length = sum(matchsticks) // 4

        def backtrack(i):

            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]

            for side in range(4):

                if sides[side] + matchsticks[i] <= single_length:
                    sides[side] += matchsticks[i]

                    if backtrack(i + 1):
                        return True

                    sides[side] -= matchsticks[i]

            return False
        
        return backtrack(0)