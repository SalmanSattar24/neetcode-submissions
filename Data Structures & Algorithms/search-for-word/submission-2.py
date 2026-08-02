class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):

            if i == len(word):
                return True
            
            directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]

            for dr, dc in directions:

                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < ROWS and 
                    0 <= nc < COLS and 
                    (nr, nc) not in visited and 
                    board[nr][nc] == word[i]
                ):

                    visited.add((nr, nc))
                    if dfs(nr, nc, i + 1):
                        return True

                    visited.remove((nr, nc))
            
            return False

        
        for r in range(ROWS):
            for c in range(COLS):

                if board[r][c] == word[0]:
                    
                    visited.add((r, c))
                    if dfs(r, c, 1):
                        return True
                    
                    visited.remove((r, c))
        
        return False
