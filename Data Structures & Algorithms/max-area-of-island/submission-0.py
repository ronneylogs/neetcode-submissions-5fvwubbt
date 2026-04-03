class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Grabs length and width of the grid
        ROWS = len(grid)
        COLS = len(grid[0])

        # Creates a set so we know which have been visited
        visited = set()

        # dfs to collect on the largest isalnd cell
        def dfs(r,c):
            if (r == ROWS or c == COLS or r<0 or c<0 or grid[r][c] == 0 or (r,c) in visited):
                return 0

            visited.add((r,c))
            return (1+dfs(r+1,c)+dfs(r,c+1)+dfs(r-1,c)+dfs(r,c-1))

        
        area = 0

        for r in range(ROWS):
            for c in range(COLS):
                area = max(area,dfs(r,c))

        return area






        # Idea is to call dfs on every cell and find the cell with the highest number of connected islands
        
        # Base case: if we step on water, if it's already visited, if we exit the map

        # choices: up down left right
            # call on each and add their values up