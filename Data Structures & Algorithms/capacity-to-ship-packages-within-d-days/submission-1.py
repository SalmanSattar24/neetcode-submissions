from typing import List

class Solution:
    """
    Time Complexity: O(N * log(S - M)), where N is the number of packages (len(weights)),
                     S is the sum of all package weights (sum(weights)), and M is the maximum package weight (max(weights)).
                     - `max(weights)` takes O(N) time.
                     - `sum(weights)` takes O(N) time.
                     - The `daysNeeded` helper function iterates through all `weights`, taking O(N) time.
                     - The binary search operates on a range from `max(weights)` to `sum(weights)`. The number of
                       iterations for binary search is log(max_capacity - min_capacity + 1), which is approximately log(S - M).
                     - In each iteration of the binary search, `daysNeeded` is called, which is O(N).
                     - Therefore, the total time complexity is O(N + N * log(S - M)) which simplifies to O(N * log(S - M)).

    Space Complexity: O(1)
                      - The space used is constant, as we are only storing a few variables like `min_capacity`,
                        `max_capacity`, `result_capacity`, `current_capacity_test`, `days_taken`, etc.
                        The `weights` list is an input and not considered additional space.
    """
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # Helper function to calculate the number of days required to ship all packages
        # given a specific `ship_capacity` (maximum weight the ship can carry per day).
        def calculateDaysTaken(ship_capacity: int) -> int:
            # `current_day_load`: Tracks the total weight loaded on the ship for the current day.
            # It starts at 0 for a new day.
            current_day_load = 0
            # `total_days_needed`: Counts the number of days required.
            # Start at 1 because we always begin on the first day.
            total_days_needed = 1

            # Iterate through each package's weight.
            for weight in weights:
                # If the current package can fit on the ship for the current day
                # (i.e., adding its weight doesn't exceed the `ship_capacity`).
                if current_day_load + weight <= ship_capacity:
                    # Add the package's weight to the current day's load.
                    current_day_load += weight
                else:
                    # If the current package cannot fit, it means a new day is required.
                    # Increment the day count.
                    total_days_needed += 1
                    # Start loading the current package onto the new day.
                    # The `current_day_load` for the new day starts with this package's weight.
                    current_day_load = weight
            
            # Return the total number of days required to ship all packages
            # with the given `ship_capacity`.
            return total_days_needed

        # Initialize the binary search range for the `ship_capacity`.
        # `lower_bound_capacity`: The minimum possible capacity the ship must have.
        # This must be at least the weight of the heaviest single package,
        # otherwise, that package could never be shipped.
        lower_bound_capacity = max(weights)
        
        # `upper_bound_capacity`: The maximum possible capacity the ship might need.
        # In the worst case, if `days` is 1, the ship must carry all packages in one go.
        # So, the sum of all weights is a valid upper bound.
        upper_bound_capacity = sum(weights)
        
        # `minimum_valid_capacity`: This variable will store the smallest valid `ship_capacity` found.
        # Initialize it to the `upper_bound_capacity` as a starting point.
        # We are looking for the minimum `ship_capacity` that satisfies the condition.
        minimum_valid_capacity = upper_bound_capacity

        # Perform a binary search to find the minimum `ship_capacity`.
        # The search space is `[lower_bound_capacity, upper_bound_capacity]`.
        while lower_bound_capacity <= upper_bound_capacity:
            # Calculate the middle capacity within the current search range.
            # This is our `current_capacity_test`.
            current_capacity_test = (lower_bound_capacity + upper_bound_capacity) // 2
            
            # Calculate the number of days required to ship all packages
            # with this `current_capacity_test`.
            days_taken = calculateDaysTaken(current_capacity_test)

            # Check if the `days_taken` with the `current_capacity_test` is greater than the allowed `days`.
            if days_taken > days:
                # If it takes too many days, it means the `current_capacity_test` is too small.
                # We need a larger capacity.
                # Discard the current capacity and all capacities below it by updating `lower_bound_capacity`.
                lower_bound_capacity = current_capacity_test + 1
            
            # If the `days_taken` is less than or equal to the allowed `days`.
            else:
                # This `current_capacity_test` is a valid capacity because we can ship within `days`.
                # Store this as a potential minimum valid capacity.
                minimum_valid_capacity = current_capacity_test
                # Now, try to find an even smaller capacity that still works.
                # Discard the current capacity and all capacities above it by updating `upper_bound_capacity`.
                upper_bound_capacity = current_capacity_test - 1
        
        # After the binary search loop, `minimum_valid_capacity` will hold the smallest
        # ship capacity that allows all packages to be shipped within the given `days`.
        return minimum_valid_capacity