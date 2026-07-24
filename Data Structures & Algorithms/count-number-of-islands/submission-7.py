class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        def bfs(r, c):

            queue = deque([(r, c)])

            while queue:

                r, c = queue.popleft()
                visited.add((r, c))

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
                        grid[nr][nc] == '1' and
                        (nr, nc ) not in visited 
                    ):
                        queue.append((nr, nc))
        
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == '1' and (r, c) not in visited:
                    
                    islands += 1
                    bfs(r, c)
        
        return islands
