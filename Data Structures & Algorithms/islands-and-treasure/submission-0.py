class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0]) 

        q = collections.deque()
        visited = set()

        dist = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))


        def addRoom(r,c):
            if r>=ROWS or r<0 or c>=COLS or c<0 or (r,c) in visited or grid[r][c] == -1:
                return
            visited.add((r,c))
            grid[r][c] = dist
            q.append([r,c])
            return

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist   
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)

                
            dist += 1




        

        # Run BFS, starting from treasure chest all at the same time

        # 1. Find out where each treasure chest is
        # 2. Create a visited set
        # 3. Create a deque for the bfs
        # 4. while the deque isn't empty process everything in that layer, inc dist each time