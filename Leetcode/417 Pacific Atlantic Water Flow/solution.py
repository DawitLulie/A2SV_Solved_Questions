class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        pacific = set()
        atlantic = set()

        def dfs(row, col, seen):
            if (row, col) in seen:
                return
            
            seen.add((row, col))

            for x, y in directions:
                nrow = row + x
                ncol = col + y

                if nrow < 0 or nrow >= rows or ncol < 0 or ncol >= cols:
                    continue
                
                if heights[nrow][ncol] >= heights[row][col]:
                    dfs(nrow, ncol, seen)

        for i in range(rows):
            dfs(i, 0, pacific)
        for j in range(cols):
            dfs(0, j, pacific)

        for i in range(rows):
            dfs(i, cols - 1, atlantic)
        for j in range(cols):
            dfs(rows - 1, j, atlantic)

        result = []
        for cell in pacific:
            if cell in atlantic:
                result.append(list(cell))

        return result