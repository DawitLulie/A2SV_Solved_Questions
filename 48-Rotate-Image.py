class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        mat = []
        for i in range(n):
            arr = []
            for j in range(n-1, -1, -1):
                arr.append(matrix[j][i])
                
            mat.append(arr)

        matrix[:] = mat

        