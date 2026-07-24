class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        INF = (2 ** 31) - 1
        
        def bfs(r, c):

            visited = set([(r, c)])
            start_r, start_c = r, c
            queue = deque([(r, c, 0)])

            while queue:

                r, c, d = queue.popleft()

                if grid[r][c] == 0:
                    grid[start_r][start_c] = d
                    return

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
                        grid[nr][nc] != -1 and 
                        (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc, d + 1))
                

        
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == INF:
                    bfs(r, c)