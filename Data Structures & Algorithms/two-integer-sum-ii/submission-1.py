class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers:
        # 'left' starts at the beginning of the list
        # 'right' starts at the end of the list
        left, right = 0, len(numbers) - 1

        # Loop continues until the two pointers cross
        while left < right:
            # Fetch current values at both pointers
            num_left, num_right = numbers[left], numbers[right]

            # Calculate their sum
            current_sum = num_left + num_right

            # Case 1: Exact match — return 1-based indices
            if current_sum == target:
                # Found the pair whose sum equals the target
                return [left + 1, right + 1]

            # Case 2: If current sum is less than target,
            # we need a larger number → move left pointer forward
            elif current_sum < target:
                left += 1

            # Case 3: If current sum is greater than target,
            # we need a smaller number → move right pointer backward
            else:
                right -= 1

        # The problem guarantees one valid solution, so this line won't be reached
        return []
