class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Initialize queue
        q = collections.deque()
        fresh = 0
        time = 0


        # All rotten vegetables to deque and find out how many fresh fruit still exist
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))



        # Iterate through queue until it is empty, each time checking 4 directions
        # Turn adjacent fresh fruit rotten and add it to deque
        # For each layer, add one unit of time

        direction = [[0,1],[1,0],[0,-1],[-1,0]]

        while fresh > 0 and q:
            length = len(q)

            for i in range(length):
                r,c = q.popleft()

                for dr, dc in direction:
                    dr = r + dr
                    dc = c + dc

                    if dr < len(grid) and dc < len(grid[0]) and dr>=0 and dc >=0:
                        if grid[dr][dc] == 1:
                            fresh -= 1
                            grid[dr][dc] = 2
                            q.append((dr,dc))
            time += 1
        
        return time if fresh == 0 else -1



        # At the end check if any fresh fruit exists, if no then return time, otherwise return -1
   








        # Idea
            # Deque to store items, everytime I visit a node, add all neighbours to the deque
            # Keep exporing until deque is empty

        # Add all rotten oranges to a queue
        # Time value to keep track of time
        # Fresh



        