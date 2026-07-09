class StockSpanner:

    def __init__(self):
        
        self.stack = []

    def next(self, price: int) -> int:

        day = 1
        
        if not self.stack or self.stack[-1][0] > price:

            self.stack.append((price, day))
            return day
        
        while self.stack and self.stack[-1][0] <= price:
            
            prev_price, prev_day = self.stack.pop()
            day += prev_day
        
        self.stack.append((price, day))
        return day



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)