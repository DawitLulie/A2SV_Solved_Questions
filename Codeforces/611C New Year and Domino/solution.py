h, w = map(int, input().split())

matrix = [list(input()) for _ in range(h)]

# Prefix sum arrays:
horizontal = [[0] * (w+1) for _ in range(h+1)]
vertical = [[0] * (w+1) for _ in range(h+1)]

# Build prefix sums
for i in range(h):
    for j in range(w):
        # Standard 2D prefix sum formula
        horizontal[i+1][j+1] = horizontal[i+1][j] + horizontal[i][j+1] - horizontal[i][j]
        vertical[i+1][j+1]   = vertical[i+1][j] + vertical[i][j+1] - vertical[i][j]

        # Check horizontal pair: (i, j-1) and (i, j)
        # If both are '.', we found a valid horizontal domino
        if j > 0 and matrix[i][j] == "." and matrix[i][j-1] == ".":
            horizontal[i+1][j+1] += 1

        # Check vertical pair: (i-1, j) and (i, j)
        # If both are '.', we found a valid vertical domino
        if i > 0 and matrix[i][j] == "." and matrix[i-1][j] == ".":
            vertical[i+1][j+1] += 1


# Number of queries
q = int(input())

for i in range(q):
    # Query rectangle (1-based indexing)
    r1, c1, r2, c2 = list(map(int, input().split()))

    # Count horizontal dominoes inside the rectangle
    hor = (horizontal[r2][c2] 
        - horizontal[r1-1][c2] 
        - horizontal[r2][c1] 
        + horizontal[r1-1][c1])

    # Count vertical dominoes inside the rectangle
    ver = (vertical[r2][c2] 
        - vertical[r1][c2] 
        - vertical[r2][c1-1] 
        + vertical[r1][c1-1])

    # Total dominoes = horizontal + vertical
    print(hor + ver)