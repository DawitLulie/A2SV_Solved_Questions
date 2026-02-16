class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []

        row = rStart
        col = cStart

        result.append([row, col])

        steps = 1
        direction = 0

        while len(result) < rows * cols:

            for _ in range(2):

                for _ in range(steps):

                    if direction == 0:
                        col += 1      # Right

                    elif direction == 1:
                        row += 1      # Down

                    elif direction == 2:
                        col -= 1      # Left
                        
                    else:
                        row -= 1      # Up

                    if 0 <= row < rows and 0 <= col < cols:
                        result.append([row, col])

                direction = (direction + 1) % 4

            steps += 1

        return result
        