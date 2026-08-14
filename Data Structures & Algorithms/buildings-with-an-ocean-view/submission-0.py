class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        n = len(heights)
        res = deque()
        res.append(n - 1)

        for i in reversed(range(n - 1)):

            h = heights[i]

            if h > heights[res[0]]:

                res.appendleft(i)
        
        return list(res)