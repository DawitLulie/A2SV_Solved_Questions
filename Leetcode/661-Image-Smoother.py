class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        smoothed = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                total = img[i][j]      # start with the center pixel
                neighbors = 1          # count itself

                # top neighbor
                if i > 0:
                    total += img[i-1][j]
                    neighbors += 1
                    # top-left
                    if j > 0:
                        total += img[i-1][j-1]
                        neighbors += 1
                    # top-right
                    if j + 1 < cols:
                        total += img[i-1][j+1]
                        neighbors += 1

                # bottom neighbor
                if i + 1 < rows:
                    total += img[i+1][j]
                    neighbors += 1
                    # bottom-left
                    if j > 0:
                        total += img[i+1][j-1]
                        neighbors += 1
                    # bottom-right
                    if j + 1 < cols:
                        total += img[i+1][j+1]
                        neighbors += 1

                # left neighbor
                if j > 0:
                    total += img[i][j-1]
                    neighbors += 1
                # right neighbor
                if j + 1 < cols:
                    total += img[i][j+1]
                    neighbors += 1

                smoothed[i][j] = total // neighbors

        return smoothed
