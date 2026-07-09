class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        heap = []

        for num in arr:

            diff = abs(num - x)
            heapq.heappush(heap, (diff, num))
        
        res = []
        for _ in range(k):
            
            diff, val = heapq.heappop(heap)

            res.append(val)
        
        return sorted(res)