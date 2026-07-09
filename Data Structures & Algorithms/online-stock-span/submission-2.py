class StockSpanner:
    def __init__(self):
        # Initialize the stack. This stack will store pairs of (price, span_value).
        # The stack will maintain elements in a way that allows us to efficiently
        # calculate the span for incoming prices. Specifically, it will store
        # prices in decreasing order. If we encounter a price smaller than or equal to
        # the top of the stack, we just push it. If we encounter a larger price,
        # we pop elements from the stack until we find a larger price or the stack is empty.
        self.price_span_stack = []

    def next(self, current_price: int) -> int:
        # Initialize the 'span_for_current_price' to 1.
        # Every stock price has a span of at least 1 (itself).
        span_for_current_price = 1

        # This loop continues as long as there are elements in the stack AND
        # the price at the top of the stack (price_span_stack[-1][0]) is less than or
        # equal to the 'current_price'.
        # This means that the stock prices at the top of the stack are "covered" by the
        # 'current_price' and should be included in its span.
        while self.price_span_stack and self.price_span_stack[-1][0] <= current_price:
            # Pop the (previous_price, previous_span) pair from the stack.
            # 'previous_price' is a price that is less than or equal to 'current_price'.
            # 'previous_span' is its already calculated span, which we can add to
            # our current span as these days also contribute to the 'current_price's span.
            prev_price, prev_span = self.price_span_stack.pop()

            # Add the 'prev_span' to 'span_for_current_price'.
            # This accumulates the consecutive days for which prices were less than or equal
            # to 'current_price'.
            span_for_current_price += prev_span

        # After the while loop finishes, either the stack is empty (meaning all previous
        # prices were less than or equal to 'current_price'), or the price at the top
        # of the stack is greater than 'current_price'.
        # In either case, we have calculated the full span for the 'current_price'.

        # Push the 'current_price' and its calculated 'span_for_current_price' onto the stack.
        # This new entry will be used for future 'next' calls.
        self.price_span_stack.append((current_price, span_for_current_price))

        # Return the calculated span for the 'current_price'.
        return span_for_current_price

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)