class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize an empty list to act as a stack for building parentheses combinations.
        stack = []
        # Initialize an empty list to store all valid parentheses combinations found.
        res = []

        # Define the recursive backtracking function.
        # open_paren: current count of open parentheses.
        # closed_paren: current count of closed parentheses.
        def backtrack(open_paren, closed_paren):
            # Base case: If both open_paren and closed_paren counts equal 'n',
            # it means we have a complete and valid combination.
            if open_paren == closed_paren == n:
                # Join the characters in the stack to form a string and add it to the results list.
                res.append(''.join(stack))
                return # End this recursive path.

            # Recursive Step 1: Add an opening parenthesis.
            # Condition: We can add an opening parenthesis if the current count
            # of open parentheses is less than 'n' (the maximum allowed).
            if open_paren < n:
                # Add an opening parenthesis to the stack.
                stack.append('(')
                # Recursively call backtrack, incrementing the open_paren count.
                backtrack(open_paren + 1, closed_paren)
                # Backtrack: Remove the last added opening parenthesis from the stack
                # to explore other possibilities. This is crucial for backtracking.
                stack.pop()

            # Recursive Step 2: Add a closing parenthesis.
            # Condition: We can add a closing parenthesis if the current count
            # of closed parentheses is less than the current count of open parentheses.
            # This ensures that we never have more closed parentheses than open ones,
            # maintaining validity.
            if closed_paren < open_paren:
                # Add a closing parenthesis to the stack.
                stack.append(')')
                # Recursively call backtrack, incrementing the closed_paren count.
                backtrack(open_paren, closed_paren + 1)
                # Backtrack: Remove the last added closing parenthesis from the stack.
                stack.pop()

        # Initial call to the backtrack function to start the process.
        # We start with 0 open and 0 closed parentheses.
        backtrack(0, 0)
        # Return the list of all valid parentheses combinations.
        return res