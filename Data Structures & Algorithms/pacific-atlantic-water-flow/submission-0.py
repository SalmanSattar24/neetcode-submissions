class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])

        def bfs(source, ocean):

            queue = source

            while queue:

                r, c = queue.popleft()
                ocean.add((r, c))

                directions = [
                    [0, 1],
                    [0, -1],
                    [1, 0],
                    [-1, 0]
                ]

                for dr, dc in directions:

                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < ROWS and 
                        0 <= nc < COLS and 
                        heights[nr][nc] >= heights[r][c] and 
                        (nr, nc) not in ocean 
                    ):

                        queue.append((nr, nc))
                        ocean.add((nr, nc))


        pacific_set, atlantic_set = set(), set()
        pacific_src = deque()
        atlantic_src = deque()

        for c in range(COLS):
            pacific_src.append((0, c))
            atlantic_src.append((ROWS - 1, c))

        for r in range(ROWS):
            pacific_src.append((r, 0))   
            atlantic_src.append((r, COLS - 1))

        bfs(pacific_src, pacific_set)
        bfs(atlantic_src, atlantic_set)

        return [i for i in pacific_set & atlantic_set]
        
