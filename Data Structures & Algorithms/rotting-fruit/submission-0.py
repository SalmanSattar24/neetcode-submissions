class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        fresh = 0


        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                    visited.add((r, c))
                
                elif grid[r][c] == 1:
                    fresh += 1

        
        time = 0
        while queue:

            r, c, t = queue.popleft()
            time = max(time, t)

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
                    grid[nr][nc] == 1
                ):

                    queue.append((nr, nc, t + 1))
                    visited.add((nr, nc))
                    fresh -= 1
        
        
        return time if fresh == 0 else -1