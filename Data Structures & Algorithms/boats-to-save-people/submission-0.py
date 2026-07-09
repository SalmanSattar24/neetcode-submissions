class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        def countingSort():
        
            min_weight, max_weight = min(people), max(people)
            counter = Counter(people)
            
            index = 0
            for weight in range(min_weight, max_weight + 1):

                if weight in counter:
                    
                    freq = counter[weight]

                    for _ in range(freq):
                        people[index] = weight
                        index += 1
        

        countingSort()

        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:

            boats += 1

            if people[left] + people[right] <= limit:
                left += 1
            
            right -= 1

        return boats