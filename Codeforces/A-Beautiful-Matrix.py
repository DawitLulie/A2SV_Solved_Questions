matrix = [list(map(int, input().split())) for _ in range(5)]
for i in range(25):
  row, col = i // 5, i % 5
  if matrix[row][col] == 1:
    print(abs(2 - row) + abs(2 - col)) 
    break

