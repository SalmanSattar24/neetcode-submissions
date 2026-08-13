class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()

        moves = 0

        for x, y in zip(seats, students):

            moves += abs(x - y)
        
        return moves