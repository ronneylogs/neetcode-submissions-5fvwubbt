class Solution:
    def solve(self, board: List[List[str]]) -> None:
        o_map = []

        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    o_map.append([r,c])

        def dfs(r,c):
            if r<0 or r>=ROWS or c<0 or c >= COLS or board[r][c] == "X" or board[r][c] == "#":
                return

            if board[r][c] == "O":
                board[r][c] = "#"
    
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # top and bottom
        for c in range(len(board[0])):
            dfs(0,c)
            dfs(len(board)-1,c)


        # left and right
        for r in range(len(board)):
            dfs(r,0)
            dfs(r,len(board[0])-1)

                
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

            

        
        # Think of a way to check the region connected to these border O's
        # Run DFS from O on the border of the matrix, mark neighbouring O's with #

        # after completing all DFS calls, we traverse the matrix again:
            # capture cells where matrix[i][j] == O
            # unmark the cells back to O where matrix[i][j] == #

        



