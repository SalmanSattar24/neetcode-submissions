class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Get the total number of days (temperatures) in the input array.
        num_days = len(temperatures)
        
        # Initialize the 'days_to_wait' array with zeros. This array will store the number of
        # days until a warmer temperature is found for each day.
        # If no warmer temperature is found in the future, the value for that day will remain 0,
        # as per the problem statement.
        days_to_wait = [0] * num_days
        
        # Initialize an empty stack.
        # This stack will store tuples of (temperature_value, original_index).
        # We'll maintain the stack such that temperatures are in monotonically decreasing order
        # from bottom to top. This means the top of the stack will always have the most
        # recent (rightmost) day with a temperature that hasn't found its warmer day yet.
        decreasing_temp_stack = [] 
        
        # Iterate through the 'temperatures' array using both the current_index (idx) and the
        # current_temperature (current_temp) for each day.
        for current_index, current_temp in enumerate(temperatures):
            # Condition 1: If the stack is empty, or the current temperature 'current_temp' is less than
            # or equal to the temperature at the top of the stack (decreasing_temp_stack[-1][0]).
            # In this case, the 'current_temp' cannot resolve any previous temperatures on the stack,
            # as it's not warmer than the top. We simply push the (current_temp, current_index) pair
            # onto the stack to maintain the monotonically decreasing order. This day will wait
            # for a future warmer temperature.
            if not decreasing_temp_stack or decreasing_temp_stack[-1][0] >= current_temp:
                decreasing_temp_stack.append((current_temp, current_index))
                continue # Move to the next temperature in the input array.
            
            # Condition 2: If the current temperature 'current_temp' is strictly warmer than the temperature
            # at the top of the stack (decreasing_temp_stack[-1][0] < current_temp).
            # This indicates that we have found a warmer temperature for one or more days whose
            # temperatures are currently on the stack and are colder than 'current_temp'.
            # We will process these days by popping them off the stack.
            while decreasing_temp_stack and decreasing_temp_stack[-1][0] < current_temp:
                # Pop the (previous_temperature_value, previous_day_index) from the stack.
                # This 'prev_temp_val' has now found its next warmer temperature, which is 'current_temp'.
                prev_temp_val, prev_day_index = decreasing_temp_stack.pop()
                
                # Calculate the number of days until a warmer temperature appears for 'prev_day_index'.
                # This is simply the difference between the 'current_index' (the index of the warmer day)
                # and the 'prev_day_index' (the index of the colder day that just found its warmer day).
                days_to_wait[prev_day_index] = current_index - prev_day_index
            
            # After popping all temperatures that are colder than the 'current_temp'
            # (or if the stack became empty during the popping process),
            # push the current (current_temp, current_index) pair onto the stack.
            # This ensures the stack continues to maintain its monotonically decreasing property
            # with the 'current_temp' now at the top (or bottom if stack was empty).
            decreasing_temp_stack.append((current_temp, current_index))
        
        # After iterating through all temperatures in the input array, the 'days_to_wait' array
        # will contain the number of days until a warmer temperature for each corresponding day.
        # Days for which no warmer temperature was found in the future will retain their initial 0 value.
        return days_to_wait