class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize the candidate element to the first number in the list
        candidate = nums[0]
        # Initialize the count to track occurrences of the candidate
        count = 1

        # Iterate through the list starting from the second element
        for i in range(1, len(nums)):
            num = nums[i]

            # If the current number is different from the candidate, decrement count
            if num != candidate:
                count -= 1
            else:
                # If the current number matches the candidate, increment count
                count += 1

            # If count reaches zero, update the candidate to the current number
            # and reset count to 1 (fixing the misspelled variable `candidiate`)
            if count == 0:
                candidate = num
                count = 1

        # Return the final candidate, which is guaranteed to be the majority element
        return candidate
