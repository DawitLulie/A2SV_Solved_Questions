n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))

cur_sum = 0
left = 0
result = 0

for right in range(n):
  cur_sum += arr[right]

  while cur_sum >= s:
    result += 1
    result += ( n - 1 - right)
    cur_sum -= arr[left]
    left += 1

print(result)


  