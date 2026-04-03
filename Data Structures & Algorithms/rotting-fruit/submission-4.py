class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotQ = collections.deque()
        

        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotQ.append((r,c))
        
        # Now we have a deque of rotten oranges and a cnt of all fresh oranges
        time = 0
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        while rotQ and fresh > 0:
 
            for i in range(len(rotQ)):
                r,c = rotQ.popleft()

                for dr,dc in direction:
                    dr += r
                    dc += c

                    if dr<len(grid) and dc<len(grid[0]) and dr>=0 and dc >=0:
                        if grid[dr][dc] == 1:
                            fresh -= 1
                            grid[dr][dc] = 2
                            rotQ.append((dr,dc))

            time += 1
        print(fresh)
        return time if fresh == 0 else -1


        




        # Idea
            # start BFS from all rotten oranges together
            # Count how many fresh oranges exist
            # each bfs layer is one unit of time
            # any fresh orange is left at the end
            # if any fresh orange is left at the end -> answer is -1
        # Algorithm
            # Initialize a queue with positions of all rotten oranges
            # Count total # of fresh oranges
            # while queue is not empty and fresh oranges exist:
                # proceed all nodes in the queue
                # for each rotten orange:
                    # check its 4 neighbourds
                    # if a neighbour is fresh:
                        # make it rotten
                        # decrease fresh count
                        # add to queue
                # increment time by 1
            # if fresh count becomes 0, return time
            # otherwise return -1, some fresh oranges still exists

        