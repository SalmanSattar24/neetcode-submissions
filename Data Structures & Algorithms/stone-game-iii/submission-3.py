class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # Increase the recursion limit to safely handle up to 50,000 elements in Python
        sys.setrecursionlimit(60000)
        
        n = len(stoneValue)
        memo = {}

        def recurse(alice, i):
            # Base Case: If there are no stones left, the score difference is 0
            if i >= n:
                return 0
            
            # Memoization key stores the current player's turn and the index
            key = (alice, i)
            if key in memo:
                return memo[key]
            
            stones_taken = 0
            
            # Initialize the worst possible outcome for the current player
            # Alice wants to maximize, so she starts at -infinity
            # Bob wants to minimize, so he starts at +infinity
            memo[key] = -math.inf if alice else math.inf

            # A player can take 1, 2, or 3 stones
            for x in range(1, 4):
                
                # Stop checking if the choice exceeds the remaining stones
                if x + i > n:
                    break
                
                # Accumulate the value of the stones taken this turn
                stones_taken += stoneValue[x + i - 1]

                if alice:
                    # ALICE'S TURN (Maximizer)
                    # She wants the highest possible net difference (Alice - Bob)
                    memo[key] = max(
                        memo[key],
                        stones_taken + recurse(not alice, i + x)
                    )

                else:
                    # BOB'S TURN (Minimizer)
                    # He wants the lowest possible net difference (Alice - Bob)
                    # We subtract stones_taken because these points go to Bob, 
                    # reducing the (Alice - Bob) advantage
                    memo[key] = min(
                        memo[key],
                        -stones_taken + recurse(not alice, i + x)
                    )
                
            return memo[key]
        
        # Start the game with Alice's turn at index 0. 
        # Returns the final (Alice - Bob) score difference.
        relative_advantage = recurse(True, 0)

        # Evaluate the final score difference to determine the winner
        if relative_advantage > 0:
            return 'Alice'
        elif relative_advantage < 0:
            return 'Bob'
        else:
            return 'Tie'