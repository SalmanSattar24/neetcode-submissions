class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize an empty list to serve as our stack.
        # This stack will temporarily hold numbers (operands)
        # as we process the Reverse Polish Notation (RPN) expression.
        stack = []

        # Iterate through each token in the input list.
        for token in tokens:
            # Check if the current token is an operator.
            # If it's '+', '-', '*', or '/', we perform an operation.
            if token == '+':
                # Pop the two most recent numbers from the stack.
                # In RPN, the operands appear before the operator.
                # 'num1' is the second operand, and 'num2' is the first operand
                # because they were pushed onto the stack in that order.
                num1 = stack.pop()  # Second operand
                num2 = stack.pop()  # First operand
                # Perform addition and push the result back onto the stack.
                stack.append(num2 + num1)

            elif token == '-':
                # Pop the two most recent numbers.
                num1 = stack.pop()  # Second operand (subtrahend)
                num2 = stack.pop()  # First operand (minuend)
                # Perform subtraction (num2 - num1) and push the result.
                stack.append(num2 - num1)

            elif token == '*':
                # Pop the two most recent numbers.
                num1 = stack.pop()  # Second operand
                num2 = stack.pop()  # First operand
                # Perform multiplication and push the result.
                stack.append(num1 * num2)

            elif token == '/':
                # Pop the two most recent numbers.
                num1 = stack.pop()  # Divisor
                num2 = stack.pop()  # Dividend
                
                # Perform division. The problem states that division
                # between integers always truncates toward zero.
                # Python's default integer division `//` performs floor division,
                # which rounds down (e.g., -3.5 becomes -4).
                # To achieve truncation towards zero (e.g., -3.5 becomes -3),
                # we convert to float, perform standard float division, then
                # convert back to an integer, which truncates the decimal part.
                stack.append(int(float(num2) / num1))

            else:
                # If the token is not an operator, it must be a number (operand).
                # Convert the string token to an integer and push it onto the stack.
                stack.append(int(token))

        # After processing all tokens, the final result of the expression
        # will be the only element remaining in the stack.
        return stack[-1]