from collections import deque

class MyStack:
    def __init__(self):
        # Initialize a deque (double-ended queue) to serve as the underlying
        # data structure. We will manipulate this deque to simulate
        # stack (Last-In, First-Out) behavior.
        self.stack = deque()

    def push(self, x: int) -> None:
        # To simulate a stack's LIFO behavior using a deque (which is inherently FIFO-like
        # when considering popleft/appendleft or pop/append from the same end),
        # we ensure that the most recently added element is always at the "front"
        # of our conceptual stack (which corresponds to one end of the deque).

        # 1. Add the new element 'x' to the left end of the deque.
        #    This temporarily places 'x' at the "front" of our deque.
        self.stack.appendleft(x)

        # 2. Now, "rotate" the existing elements to maintain the LIFO order.
        #    We move all elements that were previously in the deque
        #    from the right end to the left end. This effectively pushes
        #    them "behind" the newly added element 'x'.
        #    The loop runs for (total_elements - 1) times, because 'x' is
        #    already in its correct "top" position.
        for _ in range(len(self.stack) - 1):
            # Pop an element from the right end (back) of the deque...
            temp = self.stack.pop()
            # ...and immediately append it to the left end (front).
            self.stack.appendleft(temp)

    def pop(self) -> int:
        # To pop an element from the stack, we simply remove the element
        # that is currently at the "top" of our conceptual stack.
        # Based on our `push` implementation, the "top" element is always
        # at the right end of the deque after the rotations.
        # This acts like a standard deque's `pop()` operation.
        return self.stack.pop()

    def top(self) -> int:
        # To get the top element of the stack without removing it,
        # we peek at the element at the right end of the deque.
        # This is because `push` ensures the newest element is always
        # positioned there to be the next to be popped.
        return self.stack[-1]

    def empty(self) -> bool:
        # The stack is considered empty if the underlying deque contains no elements.
        return len(self.stack) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()         # Creates a new empty stack object
# obj.push(x)             # Adds element 'x' to the stack
# param_2 = obj.pop()     # Removes and returns the top element of the stack
# param_3 = obj.top()     # Returns the top element without removing it
# param_4 = obj.empty()   # Returns True if the stack is empty, False otherwise