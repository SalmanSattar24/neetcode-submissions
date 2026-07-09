from math import sqrt
from heapq import heappush, heappop 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclideanDistance(x, y):

            return sqrt((x - 0)**2 + (y - 0)**2)
        
        maxHeap = []

        for x, y in points:

            dist = euclideanDistance(x, y)

            heappush(maxHeap, (-dist, x, y))

            if len(maxHeap) > k:
                
                heappop(maxHeap)
        
        
        res = []
        
        for _ in range(k):

            dist, x, y = heappop(maxHeap)
            res.append([x, y])
        
        return res