class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Define rows and columns
        rows = len(board)

        cols = len(board[0])

        # Define set for collecting the path
        path = set()

        # DFS part
        def dfs(r,c,i):

            # Base case 1:
            # we found the word
            if len(word) == i:
                return True

            # Base case 2:
            # out of bounds negative, oob positive, already visited node, incorrect word
            if (min(r,c) < 0 or r>=rows or c>=cols or (r,c) in path or board[r][c] != word[i]):
                return False


            # Add it
            path.add((r,c))
            # DFS check all four directions
            res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1))
            # Remove it
            path.remove((r,c))

            return res

        # Run DFS on each cell
        for i in range(rows):
            for j in range(cols):
                if(dfs(i,j,0)==True):
                    return True
        return False

# DFS inputs
# “Where am I now?”
# “What progress have I made?”
# “What else do I need to complete the goal?”






# Note in this case we verify before adding


        