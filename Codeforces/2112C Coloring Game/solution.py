t = int(input())

for _ in range(t):
  n = int(input())

  arr = list(map(int, input().split()))
  arr.sort()

  ways = 0

  for i in range(n-1, 1, -1):
    left, right = 0, i-1

    while left < right:
      while left < right and (arr[left] + arr[right] <= arr[i] or arr[left] + arr[right] + arr[i] <= arr[-1]):
        left += 1
      if right > left:
        ways += right - left
        right -= 1

  
  print(ways)

