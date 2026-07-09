from heapq import heappush, heappop, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 1:
            return stones[0]
        
        stoneHeap = [-s for s in stones]
        heapify(stoneHeap)

        while len(stoneHeap) > 1:

            x = -heappop(stoneHeap)
            y = -heappop(stoneHeap)

            if x == y:
                continue
            
            else:

                heappush(stoneHeap, -abs(x - y))
        
        return -stoneHeap[0] if stoneHeap else 0
        