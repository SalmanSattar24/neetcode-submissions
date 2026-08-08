class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        l, r = 0, len(piles)

        memo = {}

        def recurse(l, r, alice):

            if l == r:
                return 0
            
            key = (l, r, alice)
            if key in memo:
                return memo[key]
            
            if alice:

                memo[key] = max(
                    recurse(l + 1, r, not alice) + piles[l],
                    recurse(l, r - 1, not alice) + piles[r]
                )
            
            else:

                memo[key] = min(
                    recurse(l + 1, r, not alice),
                    recurse(l, r - 1, not alice)
                )
            
            return memo[key]
        

        alice = recurse(0, r - 1, True)
        bob = sum(piles) - alice

        if alice > bob:
            return True
        
        return False