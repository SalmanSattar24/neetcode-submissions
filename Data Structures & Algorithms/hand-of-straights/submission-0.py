from _heapq import heappop
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        counter = Counter(hand)
        min_heap = list(counter.keys())
        heapq.heapify(min_heap)

        while min_heap:

            start = min_heap[0]

            for i in range(start, start + groupSize):

                if i not in counter:
                    return False

                counter[i] -= 1

                if counter[i] == 0:

                    if i != min_heap[0]:
                        return False
                    
                    heapq.heappop(min_heap)

        
        return True