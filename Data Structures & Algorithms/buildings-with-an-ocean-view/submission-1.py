class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        res = deque()

        for i, h in enumerate(heights):

            while res and heights[res[-1]] <= h:
                res.pop()

            res.append(i)
        
        return list(res)