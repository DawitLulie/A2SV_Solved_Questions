class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_row = set()
        zero_col = set()

        row = len(matrix)
        col = len(matrix[0])

        for k in range(row * col):
            i = k // col
            j = k % col

            if matrix[i][j] == 0:
                zero_row.add(i)
                zero_col.add(j)

        for k in range(row * col):
            i = k // col
            j = k % col
            
            if i in zero_row or j in zero_col:
                matrix[i][j] = 0
        