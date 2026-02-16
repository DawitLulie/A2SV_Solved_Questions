class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        diagonal = {}

        for i in range(rows):
            for j in range(cols):
                s = i + j

                if s not in diagonal:
                    diagonal[s] = []

                diagonal[s].append(mat[i][j])


        result = []

        for k in range(rows + cols - 1):

            if k % 2 == 0:
                result.extend(diagonal[k][::-1])
            else:
                result.extend(diagonal[k])


        return result

        