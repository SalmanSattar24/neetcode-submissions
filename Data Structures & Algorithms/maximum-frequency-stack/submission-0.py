class FreqStack:

    def __init__(self):
        
        self.freq_map = {}
        self.stack_of_stacks = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        
        val_freq = 1 + self.freq_map.get(val, 0)
        self.freq_map[val] = val_freq

        if val_freq > self.max_freq:

            self.max_freq = val_freq
            self.stack_of_stacks[val_freq] = []
        
        self.stack_of_stacks[val_freq].append(val)

    def pop(self) -> int:
        
        res = self.stack_of_stacks[self.max_freq].pop()
        self.freq_map[res] -= 1

        if not self.stack_of_stacks[self.max_freq]:

            self.max_freq -= 1
        
        return res



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()