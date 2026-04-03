class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        area = 0
        visited = set()

        def dfs(r,c):
            if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or (r,c) in visited:
                return 0 

            if grid[r][c] == 0:
                return 0
            
            visited.add((r,c))

            return 1+ dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    print(r,c)
                    area = max(area,dfs(r,c))
        
        return area
        

        # Idea
            # call dfs on every node that is a 1, keep track of the largest area
            # dfs
                # recurse up down and left right
                    # each time if it's a 1 add, other wise 0
                # base case is 0 return 0
