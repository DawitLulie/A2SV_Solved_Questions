t = int(input())
for _ in range(t):
  n, k = list(map(int, input().split()))
  arr = [list(map(int, input().split())) for _ in range(n)]
  arr.sort()
  for left, right, real in arr:
    if left <= k <= right and real > k:
      k = real
  print(k)
