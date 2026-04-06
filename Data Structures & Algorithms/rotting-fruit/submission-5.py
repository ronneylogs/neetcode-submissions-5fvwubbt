class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        freshC = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    freshC += 1
    
        time = 0
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]
        while freshC>0 and q:
            time += 1
            for i in range(len(q)):
                r,c = q.popleft()
                print(r,c)
            
                for dr,dc in DIRECTIONS:
                    if r+dr < len(grid) and r+dr >=0 and c+dc < len(grid[0]) and c+dc >= 0:
                        if grid[r+dr][c+dc] == 1:
                            grid[r+dr][c+dc] = 2
                            q.append((r+dr,c+dc))
                            freshC -= 1
                
        
        return time if freshC == 0 else -1
                    









        # Idea is that we will run bfs on every rotten fruit at the same time
        # for each layer we will increment time by 1


        # Algorithm
        # 1. Record location of every rotten fruit
        # 2. Record number of fresh fruit
        # 3. Add rotten fruits to deque
        # 4. Run BFS on all rotten fruits
        