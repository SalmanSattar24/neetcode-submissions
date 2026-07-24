class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        INF = (2 ** 31) - 1
        visited = set()
        queue = deque()
        




        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r,c))
        

        while queue:

            r, c, d = queue.popleft()
            grid[r][c] = d

            directions = [
                [0, 1],
                [0, -1],
                [1, 0],
                [-1, 0]
            ]

            for dr, dc in directions:

                nr, nc = dr + r, dc + c

                if (
                    0 <= nr < ROWS and 
                    0 <= nc < COLS and 
                    (nr, nc) not in visited and 
                    grid[nr][nc] != -1 
                ):

                    queue.append((nr, nc, d + 1))
                    visited.add((nr, nc))
