class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(x, y):
            
            visited.add((x, y))

            stack = collections.deque()
            stack.append((x, y))

            while stack:

                x, y = stack.popleft()
                
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

                    nx, ny = x + dx, y + dy

                    if (
                        nx >= 0 and nx < ROWS and
                        ny >= 0 and ny < COLS and
                        (nx, ny) not in visited and
                        grid[nx][ny] == '1'
                    ):
                        stack.appendleft((nx, ny))
                        visited.add((nx, ny))
        
        
        def bfs(x, y): 
            
            visited.add((x, y))

            queue = collections.deque()
            queue.append((x, y))

            while queue:

                x, y = queue.popleft()
                
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

                    nx, ny = x + dx, y + dy

                    if (
                        nx >= 0 and nx < ROWS and
                        ny >= 0 and ny < COLS and
                        (nx, ny) not in visited and
                        grid[nx][ny] == '1'
                    ):
                        queue.append((nx, ny))
                        visited.add((nx, ny))
        
        islands = 0

        for x in range(ROWS):
            for y in range(COLS):

                if (x, y) not in visited and grid[x][y] == '1':
                    
                    islands += 1
                    # bfs(x, y)
                    dfs(x, y)
        
        return islands