class MinStack:
    def __init__(self):
        # Initialize a single list (acting as a stack) to store elements.
        # Each element in this stack will be a tuple: (value, current_minimum_up_to_this_point).
        self.stack = []

    def push(self, val: int) -> None:
        # When pushing a new value 'val':
        # 1. Determine the 'current_min' for this specific state of the stack.
        #    - If the stack is currently empty, 'val' itself is the first minimum.
        #    - If the stack is not empty, the 'current_min' for this push
        #      is the minimum between the new 'val' and the minimum value
        #      associated with the previous top element of the stack.
        #      We access the previous minimum using self.stack[-1][1].
        
        # This line calculates the minimum value to be associated with the current 'val'.
        # It's the smaller of 'val' and the minimum of the stack before 'val' was pushed.
        current_min = min(val, self.stack[-1][1] if self.stack else val)
        
        # Append a tuple containing the value and its associated minimum to the stack.
        # This way, when we pop this (value, min) pair, we instantly know what the minimum
        # was up to this point, allowing O(1) getMin.
        self.stack.append((val, current_min))

    def pop(self) -> None:
        # To pop an element, simply remove the last (top) tuple from the stack.
        # This automatically removes both the value and its associated minimum.
        self.stack.pop()

    def top(self) -> int:
        # To get the top element's value, access the first element (index 0)
        # of the last tuple in the stack.
        return self.stack[-1][0]

    def getMin(self) -> int:
        # To get the current minimum element in the stack, access the second element (index 1)
        # of the last tuple in the stack. By our push logic, this element always stores
        # the minimum value among all elements currently in the stack.
        return self.stack[-1][1]