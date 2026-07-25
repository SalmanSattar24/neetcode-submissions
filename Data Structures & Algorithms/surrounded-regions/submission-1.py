class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        queue = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):

                if (
                    (r == 0 or c == 0 or 
                    r == ROWS - 1 or c == COLS - 1) and 
                    board[r][c] == 'O'
                ):
                    queue.append((r, c))
                    visited.add((r, c))

        
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
