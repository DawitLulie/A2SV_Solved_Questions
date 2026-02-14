class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        def rotate(mat):
            n = len(mat)
            new = [[0] * n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    new[i][j] = mat[n-1-j][i]

            return new


        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)

        return False
