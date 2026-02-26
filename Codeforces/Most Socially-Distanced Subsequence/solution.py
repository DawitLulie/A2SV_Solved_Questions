t = int(input())

for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))

  result = [arr[0]]
  left = 0
  right = 1

  while right < n:
    cur = left
    while right < n and arr[left] < arr[right]:
      left += 1
      right += 1

    if cur < left:
      result.append(arr[left])

    cur = left

    while right < n and arr[left] > arr[right]:
      left += 1
      right += 1

    if cur < left:
      result.append(arr[left])

  print(len(result))
  print(*result)



  
  


