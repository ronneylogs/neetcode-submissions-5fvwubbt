class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        fresh = 0
        rotten = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.add((r,c))
        
        q = collections.deque()

        # add initial rotten items to q
        for i in rotten:
            q.append(i)

        DIRECTIONS = [[1,0],[-1,0],[0,1],[0,-1]]
        
        time = 0
        while q and fresh>0:
            time +=1

            for b in range(len(q)):
                i = q.popleft()

                for dr,dc in DIRECTIONS:
                    dr += i[0]
                    dc += i[1]
                    if (dr,dc) in rotten or dr < 0 or dr >= ROWS or dc < 0 or dc >= COLS or grid[dr][dc] == 0:
                        continue

                    fresh -=1
                    grid[dr][dc] = 2
                    rotten.add((dr,dc))
                    q.append((dr,dc))
                    
        print(fresh)
        return time if fresh==0 else -1



        



    # Idea
        # start from all rotten bananas and only expand to cells that have a fresh banana
        # Use bfs, each layer, add one minute
        # we stop when we run out of fresh bananas, or we run out of items in the bfs queue (banana unreachable)

    # Algorithm
        # count the total of fresh banana
        # grab coordinates of rotten bananas, add to queue
        # Set time to 0
        # Use BFS to expand to infect all fresh bananas
            # need a set to track rotten bananas
