class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Step 1: Combine the initial position and speed for each car.
        # 'cars_data' will store tuples, each containing (initial_position, initial_speed).
        # This pairing helps to keep each car's related information together for easier processing.
        cars_data = []
        for i in range(len(position)):
            cars_data.append((position[i], speed[i]))

        # Step 2: Sort the 'cars_data' list based on the cars' initial positions.
        # The sorting is done in descending order ('reverse=True') by position (x[0] in the lambda).
        # This sorting strategy is critical for the algorithm: it allows us to analyze cars
        # from the one closest to the destination backwards. This simplifies fleet detection
        # because a car can only merge with a fleet that is already ahead of it.
        cars_data.sort(key=lambda x: x[0], reverse=True)

        # Step 3: Initialize a stack and a counter for the number of fleets.
        # The 'fleet_times' stack will store the calculated arrival time at the 'target'
        # for the leading car of each distinct fleet.
        # The 'num_fleets' variable will explicitly count the total number of car fleets.
        fleet_times = []
        num_fleets = 0 # This variable will be used to count fleets according to your specific logic.

        # Step 4: Iterate through the sorted 'cars_data' to determine fleet formation.
        # 'car_pos' represents the current car's initial position.
        # 'car_speed' represents the current car's constant speed.
        for car_pos, car_speed in cars_data:
            # Calculate the time it takes for the current car to reach the 'target' destination.
            # Time is calculated as: (Distance to Target) / Speed.
            # The distance for the current car is: (target - car_pos).
            current_car_arrival_time = (target - car_pos) / car_speed

            # Step 5: Apply your precise logic for fleet formation and counting.
            # This 'if' condition checks if the 'fleet_times' stack is NOT empty AND
            # if the 'current_car_arrival_time' is less than or equal to the arrival time
            # of the fleet leader currently at the top of the stack (fleet_times[-1]).
            # If this condition is true, it indicates that the current car will reach the destination
            # at the same time as, or faster than, the fleet directly in front of it.
            # Since cars cannot pass, this car will catch up and join that existing fleet.
            if fleet_times and current_car_arrival_time <= fleet_times[-1]:
                # Action for merging: When the current car merges into an existing fleet,
                # no new distinct fleet is formed. Therefore, the stack is unchanged,
                # and 'num_fleets' is not incremented here.
                pass
            # Else (this block executes if the 'fleet_times' stack is empty,
            # OR if 'current_car_arrival_time' is strictly greater than the top of the stack):
            # This means either this car is the very first to form a fleet (stack is empty),
            # or it's slower than the fleet ahead of it. In both scenarios, it begins a new, distinct fleet.
            else:
                # Action for a new fleet:
                # 1. Increment 'num_fleets' because a new distinct fleet has been identified.
                num_fleets += 1
                # 2. Append the 'current_car_arrival_time' to the stack. This time now represents
                #    the arrival time of this newly formed fleet's leading car.
                fleet_times.append(current_car_arrival_time)

        # Step 6: Return the final count of car fleets.
        # Your code explicitly returns the value stored in the 'num_fleets' variable,
        # which was incremented each time a new fleet was determined to form.
        return num_fleets