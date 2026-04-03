class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(x,y):
            if x > len(grid)-1 or y > len(grid[0])-1 or x < 0 or y < 0:
                return
            if grid[x][y] == "1":
                grid[x][y] = "0"
                dfs(x+1,y)
                dfs(x,y+1)
                dfs(x,y-1)
                dfs(x-1,y)
           

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)

        return count
        

        


        # The idea is that we will run dfs on a single node, explore left, right, up, down, then
        # mark that pos as visited by turning them into 0s

        # Walk through the rest of grid and run dfs on each node unless it's already visited

        # Each time I walk onto an unvisited node that has 1, I will increment my counter