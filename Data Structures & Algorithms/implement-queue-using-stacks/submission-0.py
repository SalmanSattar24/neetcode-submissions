class MyQueue:

    def __init__(self):
        
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        
        self.push_stack.append(x)

    def pop(self) -> int:
        
        if self.pop_stack:
            return self.pop_stack.pop()
        
        if not self.pop_stack and self.push_stack:
            
            self.moveToPopStack()

            return self.pop_stack.pop() 

    def peek(self) -> int:

        if self.pop_stack:
            return self.pop_stack[-1]
        
        elif not self.pop_stack and self.push_stack:

            self.moveToPopStack()

            return self.pop_stack[-1]
        

    def empty(self) -> bool:

        if not self.pop_stack and not self.push_stack:
            return True
        
        return False


    def moveToPopStack(self) -> None:

        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()