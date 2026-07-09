from heapq import heappush, heappop
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = Counter(tasks)
        maxHeap = [-freq for freq in counter.values()]
        queue = deque()
        time = 0

        while maxHeap or queue:

            time += 1

            if queue and queue[0][1] < time:

                heappush(maxHeap, queue.popleft()[0])

            if maxHeap:

                numTask = heappop(maxHeap)
                numTask += 1

                if numTask:

                    queue.append((numTask, time + n))
        
                
        return time