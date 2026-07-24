class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        perimeter = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                if grid[r][c] == 0:
                    continue

                cell_perimeter = 4

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:

                    neighbour_r, neighbour_c = r + dr, c + dc

                    if (
                        0 <= neighbour_r < len(grid) and
                        0 <= neighbour_c < len(grid[0]) and
                        grid[neighbour_r][neighbour_c] == 1
                    ):
                        cell_perimeter -= 1
                
                perimeter += cell_perimeter
        
        return perimeter