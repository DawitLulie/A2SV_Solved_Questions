class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(row, col):
            if board[row][col] != "O":
                return
            
            board[row][col] = "S"

            for x, y in directions:
                nrow = row + x
                ncol = col + y

                if 0 <= nrow < rows and 0 <= ncol < cols:
                    dfs(nrow, ncol)

        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)
        
        for i in range(cols):
            dfs(0, i)
            dfs(rows-1, i)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"