class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        sorted_positions = sorted(position.copy(), reverse=True)
        
        position_speed_array = []

        for i in range(len(position)):

            position_speed_array.append((position[i], speed[i]))
        
        position_speed_array = sorted(position_speed_array, key = lambda x : x[0], reverse=True)

        stack = []
        fleets = 0

        for pos, speed in position_speed_array:

            time = (target - pos) / speed

            if stack and time <= stack[-1]:
                pass
            
            else:
                fleets += 1
                stack.append(time)

        return fleets