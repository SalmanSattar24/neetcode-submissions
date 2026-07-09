from collections import deque

class MyQueue:
    def __init__(self):
        # Initialize two lists to act as our stacks.
        # push_stack will primarily be used for adding new elements.
        # pop_stack will primarily be used for removing and peeking elements,
        # ensuring FIFO order.
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        # Add the new element 'x' to the top of the push_stack.
        # This is a standard stack push operation.
        self.push_stack.append(x)

    def pop(self) -> int:
        # Before popping, ensure that pop_stack has elements.
        # If pop_stack is empty, it means we need to transfer elements
        # from push_stack to pop_stack to reverse their order and maintain FIFO.
        if not self.pop_stack:
            self.moveToPopStack()
        
        # If pop_stack is still empty after potential transfer (meaning the queue is truly empty),
        # this case is generally handled by problem constraints that guarantee valid calls.
        # Otherwise, we would raise an error or return a special value.
        
        # Pop and return the element from the top of the pop_stack.
        # This element will be the front of our conceptual queue due to the transfer logic.
        return self.pop_stack.pop()

    def peek(self) -> int:
        # Similar to pop, ensure pop_stack is populated for peeking.
        if not self.pop_stack:
            self.moveToPopStack()
        
        # Return the top element of the pop_stack without removing it.
        # This element is the front of our conceptual queue.
        # In Python lists, -1 accesses the last element (the top of the stack).
        return self.pop_stack[-1]

    def empty(self) -> bool:
        # The queue is empty if both the push_stack and pop_stack are empty.
        # If elements exist in either, the queue is not empty.
        if not self.pop_stack and not self.push_stack:
            return True
        return False

    def moveToPopStack(self) -> None:
        # This helper method transfers all elements from push_stack to pop_stack.
        # This is crucial for maintaining the FIFO order when performing pop or peek.
        # Elements popped from push_stack (LIFO) are appended to pop_stack,
        # effectively reversing their order and making the oldest element
        # (first pushed into push_stack) appear at the top of pop_stack.
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top() # Note: The example uses .top() but the class has .peek().
#                    # Assuming .top() here refers to .peek().
# param_4 = obj.empty()