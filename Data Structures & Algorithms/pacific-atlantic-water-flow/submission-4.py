class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        res = []

        def dfs(r,c,prevHeight,visited):
            if r<0 or r>=ROWS or c<0 or c>=COLS or heights[r][c] < prevHeight or (r,c) in visited:
                return

            visited.add((r,c))

            dfs(r+1,c,heights[r][c],visited)
            dfs(r-1,c,heights[r][c],visited)
            dfs(r,c+1,heights[r][c],visited)
            dfs(r,c-1,heights[r][c],visited)

            return
        

        # run through top and bottom
        for i in range(len(heights[0])):
            # top
            dfs(0,i,heights[0][i],pacific)

            # bottom
            dfs(ROWS-1,i,heights[ROWS-1][i],atlantic)
           

        # run through right and left
        for i in range(len(heights)):
            # left
            dfs(i,0,heights[i][0],pacific)

            # right
            dfs(i,COLS-1,heights[i][COLS-1],atlantic)


        # check through every cell to see if it's in both atlantic and pacific, if yes then add to res
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append([r,c])

        return res

        


    

    # Call DFS from the borders, twice for each cell to test both atlantic and pacific
        # base cases
            # out of bounds
            # already visited
            # or it's not increasing in height
    # create a set for atlantic and a set for pacific, if answer is in both then add it to final res
    
