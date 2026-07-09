import math
from typing import List

class Solution:
    """
    Time Complexity: O(N * log(MaxP)), where N is the number of piles and MaxP is the maximum value in `piles`.
                     - `max(piles)` takes O(N) time to find the largest pile.
                     - The `eatingTime` function iterates through all piles, taking O(N) time.
                     - The binary search operates on a range from 1 to `max(piles)`. The number of iterations for
                       binary search is log(MaxP), where MaxP is `max(piles)`.
                     - In each iteration of the binary search, `eatingTime` is called, which is O(N).
                     - Therefore, the total time complexity is O(N + N * log(MaxP)) which simplifies to O(N * log(MaxP)).

    Space Complexity: O(1)
                      - The space used is constant, as we are only storing a few variables like `min_rate`,
                        `max_rate`, `k`, `new_rate`, and `time_needed`. The `piles` list is an input and not considered
                        additional space.
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Initialize the search range for the eating rate 'k'.
        # min_rate: The slowest possible eating rate is 1 banana per hour. Koko must eat at least 1.
        # max_rate: The fastest possible eating rate is the size of the largest pile.
        #           If Koko eats at a rate equal to the largest pile, she finishes that pile in 1 hour.
        #           Eating any faster than max(piles) would not reduce the total time, as each pile
        #           would still be consumed in 1 hour if k >= pile_size.
        min_rate, max_rate = 1, max(piles)
        
        # Initialize 'k' (the minimum eating speed) to the maximum possible rate.
        # This variable will store the best (minimum) valid eating speed found so far.
        # We start it at the upper bound because we are looking for the minimum valid 'k'.
        # Any 'k' that allows Koko to finish within 'h' hours could be a candidate,
        # and we want the smallest such 'k'.
        k = max_rate

        # Define a helper function to calculate the total time needed to eat all piles
        # given a specific eating 'rate'.
        def eatingTime(rate):
            # Initialize total time to 0.
            time = 0

            # Iterate through each pile of bananas.
            for pile in piles:
                # Calculate the time needed for the current pile.
                # We use math.ceil(float(pile) / rate) because Koko eats a full pile even if there are
                # only a few bananas left. For example, if pile is 7 and rate is 3,
                # it takes ceil(7/3) = ceil(2.33) = 3 hours.
                # We cast `pile` to `float` to ensure floating-point division
                # before applying `math.ceil()`. This is crucial for correct ceiling behavior.
                time += math.ceil(float(pile) / rate)
            
            # Return the total time taken for all piles at the given rate.
            return time

        # Perform a binary search to find the minimum eating speed 'k'.
        # The search space for 'k' is `[min_rate, max_rate]`.
        # This loop continues as long as there is a valid search range.
        while min_rate <= max_rate:
            # Calculate the middle rate (potential 'k') within the current search range.
            # Using integer division `//` ensures `new_rate` remains an integer.
            new_rate = (min_rate + max_rate) // 2
            
            # Calculate the total time needed to eat all bananas at this `new_rate`.
            time_needed = eatingTime(new_rate)

            # Check if the `time_needed` at the `new_rate` is greater than the allowed time `h`.
            if time_needed > h:
                # If `time_needed` is too long, it means `new_rate` is too slow.
                # Koko needs to eat faster.
                # Therefore, we discard the current `new_rate` and all rates below it,
                # updating `min_rate` to `new_rate + 1` to search in the upper half.
                min_rate = new_rate + 1
            
            # If the `time_needed` is less than or equal to 'h'.
            else:
                # This `new_rate` is a valid eating speed because Koko can finish within 'h' hours.
                # It's a potential answer, so we store it in `k`.
                k = new_rate
                # Now, we try to find an even smaller (more optimal) rate.
                # We discard the current `new_rate` and all rates above it,
                # updating `max_rate` to `new_rate - 1` to search in the lower half.
                # This is because we've found a valid `k`, but there might be a smaller `k` that also works.
                max_rate = new_rate - 1
        
        # After the binary search loop, `k` will hold the minimum eating speed
        # at which Koko can finish all bananas within 'h' hours.
        # The loop terminates when `min_rate` becomes greater than `max_rate`,
        # at which point `k` will contain the lowest valid rate found.
        return k