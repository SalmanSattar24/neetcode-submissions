from collections import Counter # This import needs to be at the top of your Python file

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Calculates the minimum number of boats required to save all people,
        given their weights and a boat's weight limit.

        Each boat can carry at most two people, provided their combined weight
        does not exceed the limit.

        Time Complexity:
        O(N + MaxWeight - MinWeight) for the counting sort part, where N is the
        number of people, MaxWeight is the maximum weight, and MinWeight is the
        minimum weight. In the worst case (MaxWeight - MinWeight is large),
        this can approach O(limit) since weights are capped by `limit`.
        O(N) for the two-pointer part.
        Overall, the dominant factor is the counting sort, so O(N + limit).

        Space Complexity:
        O(MaxWeight - MinWeight) for the `weight_counts` dictionary (or array if using a fixed-size array).
        This can approach O(limit) in the worst case.
        """

        # --- Counting Sort Implementation ---
        # This section sorts the 'people' array in-place using a counting sort approach.
        # This is an alternative to Python's built-in `people.sort()` which is O(N log N).

        # Handle edge case: if there are no people, no boats are needed.
        if not people:
            return 0

        # 1. Determine the range of weights and count frequencies.
        # Initialize min_weight and max_weight to find the actual range in the input.
        min_weight = float('inf')
        max_weight = float('-inf')

        # Iterate through the input 'people' to find the actual min and max weights.
        for weight in people:
            min_weight = min(min_weight, weight)
            max_weight = max(max_weight, weight)

        # Count occurrences of each weight.
        # Using collections.Counter is an efficient way to get frequencies.
        weight_counts = Counter(people)

        # 2. Reconstruct the sorted 'people' array in-place.
        # 'current_write_index' tracks the next available position in the 'people' array
        # where a sorted weight should be placed.
        current_write_index = 0
        # Iterate from the minimum observed weight to the maximum observed weight.
        for weight_val in range(min_weight, max_weight + 1):
            # If the current 'weight_val' exists in our counts, process it.
            if weight_val in weight_counts:
                frequency = weight_counts[weight_val]
                # Place 'weight_val' into the 'people' array 'frequency' times.
                for _ in range(frequency):
                    people[current_write_index] = weight_val
                    current_write_index += 1

        # --- Two-Pointer Greedy Algorithm (applied after sorting) ---
        # Now that the 'people' array is sorted by weight, we can apply the two-pointer strategy
        # to find the minimum number of boats.

        left_ptr = 0                # Pointer for the lightest person (starts at the beginning)
        right_ptr = len(people) - 1 # Pointer for the heaviest person (starts at the end)
        boats_needed = 0            # Counter for the total number of boats required

        # Continue the process as long as there are people left to be boated.
        # The loop runs until the pointers cross or meet.
        while left_ptr <= right_ptr:
            boats_needed += 1 # Always launch a new boat for the current heaviest person (right_ptr).

            # Check if the lightest person (left_ptr) can share the boat with
            # the heaviest person (right_ptr) without exceeding the 'limit'.
            if people[left_ptr] + people[right_ptr] <= limit:
                left_ptr += 1 # If they fit, the lightest person also boards, so move this pointer inward.

            # The heaviest person always boards the current boat (either alone or with the lighter person).
            # So, move the right pointer inward regardless of whether the lighter person joined.
            right_ptr -= 1

        return boats_needed