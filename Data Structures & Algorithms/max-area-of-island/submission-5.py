class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):

            queue = deque([(r, c)])
            size = 1

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

                    nr, nc = dr + r, dc + c

                    if (
                        0 <= nr < ROWS and 
                        0 <= nc < COLS and 
                        grid[nr][nc] == 1 and 
                        (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        size += 1

            
            return size
                

        max_island = 0

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 1 and (r, c) not in visited:
                    max_island = max(max_island, bfs(r, c))
        
        return max_island