from heapq import heappush, heappop
from collections import Counter
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task using Counter
        counter = Counter(tasks)

        # Create a max-heap by pushing negative frequencies (since Python's heapq is a min-heap)
        maxHeap = [-freq for freq in counter.values()]

        # Initialize a queue to keep track of tasks on cooldown
        # Each queue element is a tuple: (remaining frequency, time when it can be reinserted)
        queue = deque()

        # Initialize the total time taken
        time = 0

        # Loop until both the heap and queue are empty
        while maxHeap or queue:
            # Increment the time at each iteration (simulating a time unit)
            time += 1

            # Check if any task in the queue has finished its cooldown
            if queue and queue[0][1] < time:
                # If so, reinsert it into the heap
                heappush(maxHeap, queue.popleft()[0])

            # If there are tasks in the heap, process the most frequent one
            if maxHeap:
                # Pop the most frequent task (using negative values for max-heap simulation)
                numTask = heappop(maxHeap)

                # Decrement the frequency (since we're processing one occurrence)
                numTask += 1

                # If there are remaining occurrences, add it to the queue with a cooldown time
                if numTask:
                    queue.append((numTask, time + n))

        # Return the total time taken to complete all tasks
        return time
