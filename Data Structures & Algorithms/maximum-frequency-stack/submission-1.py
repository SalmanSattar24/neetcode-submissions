class FreqStack:
    def __init__(self):
        # freq_map: This dictionary stores the frequency of each number.
        # Key: The number itself.
        # Value: The frequency of that number in the stack.
        self.freq_map = {}

        # stack_of_stacks: This dictionary organizes numbers into "stacks" based on their frequency.
        # Key: The frequency (e.g., 1 for numbers appearing once, 2 for numbers appearing twice, etc.).
        # Value: A list (acting as a stack) containing numbers that currently have this frequency.
        # Numbers are appended to the end of the list when pushed, and popped from the end.
        self.stack_of_stacks = {}

        # max_freq: This integer keeps track of the highest frequency encountered so far among all numbers.
        # This allows for efficient retrieval of the most frequent elements during a pop operation.
        self.max_freq = 0

    def push(self, val: int) -> None:
        # Time Complexity: O(1)
        # Space Complexity: O(1) (amortized, for new unique values)

        # Increment the frequency of the pushed value.
        # If the value is not in freq_map, .get(val, 0) returns 0, so val_freq becomes 1.
        val_freq = 1 + self.freq_map.get(val, 0)
        self.freq_map[val] = val_freq

        # Update max_freq if the current value's frequency is higher.
        if val_freq > self.max_freq:
            self.max_freq = val_freq

        # If there's no stack for the current frequency, create one.
        if val_freq not in self.stack_of_stacks:
            self.stack_of_stacks[val_freq] = []

        # Add the value to the stack corresponding to its current frequency.
        self.stack_of_stacks[val_freq].append(val)

    def pop(self) -> int:
        # Time Complexity: O(1)
        # Space Complexity: O(1)

        # Retrieve the most frequent element.
        # This element is the last one pushed into the stack corresponding to max_freq.
        popped_val = self.stack_of_stacks[self.max_freq].pop()

        # Decrement the frequency of the popped value in freq_map.
        self.freq_map[popped_val] -= 1

        # If the stack for the current max_freq becomes empty after popping,
        # it means no numbers currently have this frequency, so decrement max_freq.
        if not self.stack_of_stacks[self.max_freq]:
            self.max_freq -= 1

        # Return the popped value.
        return popped_val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()