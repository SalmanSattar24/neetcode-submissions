from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # Early termination: If the starting position or the target destination 
        # is a '1' (a stone), it's impossible to start or finish the game.
        if s[0] == '1' or s[-1] == '1':
            return False

        n = len(s)
        
        # Initialize a queue for Breadth-First Search (BFS) 
        # to track the indices we have successfully landed on.
        queue = deque()
        
        # A set to keep track of indices we've already added to the queue
        # to prevent processing the same index multiple times.
        visited = set()
        
        # Start the BFS from the first index
        queue.append(0)

        while queue:
            # Pop the current index we are jumping from
            reach = queue.popleft()

            # Calculate the minimum and maximum indices we can reach from here
            start = reach + minJump
            
            # Cap the maximum jump to the end of the string to avoid out-of-bounds errors
            end = min(reach + maxJump, n - 1)

            # Check every possible landing spot within our jump range
            for i in range(start, end + 1):
                
                # We can only land on a '0'
                if s[i] == '0':
                    
                    # If we just landed on the final index, we won!
                    if i == n - 1:
                        return True
                        
                    # If it's a valid landing spot we haven't explored yet,
                    # queue it up so we can jump from it later.
                    if i not in visited:
                        queue.append(i)
                        visited.add(i)
                        
        # If the queue empties out and we never reached the end, it's impossible.
        return False