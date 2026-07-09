class Solution:
    def decodeString(self, s: str) -> str:
        # Time Complexity: O(N) where N is the length of the string 's'.
        # In the worst case, we iterate through the string once.
        # String concatenation and stack operations take amortized constant time.
        # However, the string multiplication (decoded_string * num) can take
        # time proportional to the length of the resulting string segment,
        # but overall, each character from the input contributes a constant
        # amount to the final output string construction.

        # Space Complexity: O(N) in the worst case.
        # The stack can grow up to a depth proportional to the number of nested brackets.
        # The strings stored on the stack can also contribute to space usage.
        # In the worst case, the decoded string itself can be very long (e.g., if k is large
        # and there are many repetitions), and it's being built in decoded_string.
        # The maximum size of the stack and the temporary strings stored would be
        # proportional to the length of the input string 's' in a highly nested scenario.

 # Initialize a stack to keep track of previous states (strings and numbers)
        # when we encounter nested encoded sequences.
        stack = []

        # Initialize `current_num` to accumulate digits for the repetition count (k).
        # For example, if we see '1' then '2', current_num becomes 12.
        current_num = 0

        # Initialize `current_string` to build the current decoded string segment.
        # This string accumulates characters within the current level of brackets,
        # or outside any brackets.
        current_string = ""

        # Iterate through each character in the input string 's'.
        for char in s:
            # Case 1: If the character is a digit.
            if char.isdigit():
                # Convert the character to an integer and append it to `current_num`.
                # This handles multi-digit numbers (e.g., '10', '300').
                current_num = current_num * 10 + int(char)
            # Case 2: If the character is an opening square bracket '['.
            elif char == '[':
                # When we encounter '[', it means we are starting a new
                # inner encoded sequence. We need to save the state of
                # the string we were building so far (`current_string`)
                # and the repetition count that applies to this new inner sequence
                # (`current_num`).

                # Push the `current_string` onto the stack. This is the part of
                # the string that comes *before* the new bracketed segment.
                stack.append(current_string)

                # Push the `current_num` onto the stack. This is the repetition
                # factor for the *new* segment that is about to be decoded.
                stack.append(current_num)

                # Reset `current_string` to an empty string. This is because we are
                # starting to build a *new* string segment that will be inside
                # the current brackets.
                current_string = ""

                # Reset `current_num` to 0. This is to start accumulating the
                # repetition count for any *further nested* segments within
                # the current brackets.
                current_num = 0
            # Case 3: If the character is a closing square bracket ']'.
            elif char == ']':
                # When we encounter ']', it signifies the end of an encoded sequence.
                # We now need to retrieve the saved state from the stack to
                # construct the decoded string for this segment.

                # Pop the last number from the stack. This is the `k` (repetition count)
                # for the segment that has just finished being processed inside the brackets.
                num = stack.pop()

                # Pop the previous string from the stack. This is the string content
                # that was accumulated *before* the opening bracket of the current segment.
                prev_string = stack.pop()

                # Now, combine the `prev_string` with the repeated `current_string`.
                # `current_string` at this point holds the fully decoded content
                # of the segment that was *just* inside the brackets (e.g., "b" for "3[b]").
                # `current_string * num` repeats this decoded content `num` times
                # (e.g., "bbb").
                # This repeated content is then concatenated with `prev_string`
                # (e.g., "a" + "bbb" -> "abbb").
                # The result becomes the new `current_string`, effectively appending
                # the decoded segment to the string being built at the outer level.
                current_string = prev_string + current_string * num
            # Case 4: If the character is a lowercase English letter.
            else:
                # If it's a regular letter, simply append it to the `current_string`.
                # These are characters that are not part of a repetition or bracket
                # structure at the current level (e.g., 'c' in "2[a3[b]]c").
                current_string += char
        
        # After iterating through all characters in the input string 's',
        # `current_string` will contain the final, completely decoded string.
        return current_string