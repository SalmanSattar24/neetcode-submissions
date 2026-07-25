class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        queue = deque()
        visited = set()

        for r in range(ROWS):

            if board[r][0] == 'O':
                queue.append((r, 0))
                visited.add((r, 0))
            
            if board[r][COLS - 1] == 'O':
                queue.append((r, COLS - 1))
                visited.add((r, COLS - 1))
        
        for c in range(COLS):

            if board[0][c] == 'O':
                queue.append((0, c))
                visited.add((0, c))
            
            if board[ROWS - 1][c] == 'O':
                queue.append((ROWS - 1, c))
                visited.add((ROWS - 1, c))

        
        while queue:

            r, c = queue.popleft()

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
                    (nr, nc) not in visited and 
                    board[nr][nc] == 'O'
                ):
                    queue.append((nr, nc))
                    visited.add((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):

                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'
