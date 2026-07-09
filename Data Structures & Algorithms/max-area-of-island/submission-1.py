class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            size = 0
            queue = collections.deque([(r, c)])
            visited.add((r, c))

            while queue:
                r, c = queue.popleft()
                size += 1

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visited and
                        grid[nr][nc] == 1
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return size

        max_size = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_size = max(max_size, bfs(r, c))

        return max_size