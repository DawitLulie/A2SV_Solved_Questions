class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negative = 0
        for row in grid:
            i = len(row) - 1
            while  i >= 0 and row[i] < 0:
                negative += 1
                i -= 1

        return negative


        