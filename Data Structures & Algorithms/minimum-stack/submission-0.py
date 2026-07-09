class MinStack:

    def __init__(self):
        
        self.stack = []

    def push(self, val: int) -> None:
        
        last_min = self.stack[-1][1] if self.stack else val

        current_min = min(val, last_min)

        self.stack.append((val, current_min))

    def pop(self) -> None:
        
        self.stack.pop()


    def top(self) -> int:
        
        return self.stack[-1][0]

    def getMin(self) -> int:
        
        return self.stack[-1][1]
