class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshC = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        rot = set()
        # Find coordinates of rotten oranges and count number of fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshC +=1
                elif grid[r][c] == 2:
                    rot.add((r,c))
        
        q = collections.deque()
        for c in rot:
            q.append(c)
        DIRECTIONS = [[0,1],[1,0],[0,-1],[-1,0]]
        time = 0
        while q and freshC >0:
            time +=1
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in DIRECTIONS:
                    dr += r
                    dc += c

                    if  dr < ROWS and dr >= 0 and dc < COLS and dc >= 0 and grid[dr][dc] == 1:
                        freshC -= 1
                        grid[dr][dc] = 2
                        q.append((dr,dc))
        print(freshC)
        return time if freshC == 0 else -1



                

        


        # Find out coordinates of rotten fruit, call bfs on each rotten fruit all at the same time

        # use a time value, each level is a time value

        # stop bfs when we run out of fresh fruits or if we run out of items to expand to