class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] # Initialize an empty stack to store surviving asteroids.

        # Iterate through each asteroid in the input array.
        for ast in asteroids:
            # Handle collisions: This loop continues as long as a collision is possible.
            # A collision occurs if:
            # 1. The stack is not empty (there's an asteroid to collide with).
            # 2. The top asteroid on the stack is moving right (positive).
            # 3. The current incoming asteroid is moving left (negative).
            while stack and stack[-1] > 0 and ast < 0:
                top_asteroid_size = stack[-1]       # Size of the asteroid at the top of the stack.
                current_asteroid_size = abs(ast)    # Absolute size of the incoming asteroid for comparison.

                # Case 1: The asteroid on the stack is larger.
                # The incoming asteroid 'ast' explodes.
                if top_asteroid_size > current_asteroid_size:
                    ast = 0  # Mark 'ast' as destroyed so it won't be added to the stack.
                    break    # No further collisions for this 'ast', exit inner loop.

                # Case 2: The incoming asteroid is larger.
                # The asteroid on the stack explodes.
                elif current_asteroid_size > top_asteroid_size:
                    stack.pop() # Remove the exploded asteroid from the stack.
                    # Continue the loop to check 'ast' against the next asteroid on the stack.

                # Case 3: Both asteroids are of the same size.
                # Both asteroids explode.
                else: # current_asteroid_size == top_asteroid_size
                    stack.pop() # Remove the exploded asteroid from the stack.
                    ast = 0     # Mark 'ast' as destroyed.
                    break       # Both are gone, exit inner loop.

            # After checking for all potential collisions with asteroids currently in the stack,
            # if the current asteroid 'ast' has not been destroyed (i.e., its value is not 0),
            # it means it survived or moved in a non-colliding direction.
            # Add it to the stack.
            if ast != 0:
                stack.append(ast)

        # The remaining asteroids in the stack represent the final state.
        return stack