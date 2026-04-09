class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        visited = set()

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        dist = 0
        DIRECTIONS = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                for dr,dc in DIRECTIONS:
                    dr += r
                    dc += c

                    if dr<0 or dr>=ROWS or dc<0 or dc>=COLUMNS or (dr,dc) in visited or grid[dr][dc] == -1:
                        continue
                    
                    visited.add((dr,dc))
                    q.append([dr,dc])
            
            dist += 1

        return
            
  


        

        # Run BFS, starting from treasure chest all at the same time

        # 1. Find out where each treasure chest is
        # 2. Create a visited set
        # 3. Create a deque for the bfs
        # 4. while the deque isn't empty process everything in that layer, inc dist each time