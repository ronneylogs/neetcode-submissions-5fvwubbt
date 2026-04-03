class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        def dfs(r,c):
            # if r,c is invalid
            if (r == ROWS or r<0 or c==COLS or c<0 or (r,c) in visited or grid[r][c]==0):
                return 0


            # add to visited
            visited.add((r,c))
            

            # run dfs on those
            area = 1+ dfs(r+1,c) + dfs(r-1,c) + dfs(r,c-1) + dfs(r,c+1)

            return area


    
        # Run dfs on each cell
            # dfs take in a cell
            # Return should give 1 to add up the number of cells that are connected
    
        ret = 0
        for r in range(ROWS):
            for c in range(COLS):
                ret = max(ret,dfs(r,c))
        
        return ret




    
    # IDEA: We can run dfs on each cell in the grid and record highest mark