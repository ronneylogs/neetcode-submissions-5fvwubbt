class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        path = set()
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r,c,i):
            if len(word) == i:
                return True
            
            # base case 2: out of bounds
            if r < 0 or r >=ROWS or c<0 or c>=COLS or (r,c) in path or board[r][c] != word[i]:
                return False
            
            # matches
            path.add((r,c))

            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)

            path.remove((r,c))

            return res
        


        # idea
        # run dfs on each cell

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0) == True:
                    return True
            
        return False
                    
    
