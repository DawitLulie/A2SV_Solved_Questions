n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))

cur_sum = 0
left = 0
max_len = 0

for right in range(len(arr)):
  cur_sum += arr[right]
  while cur_sum > s:
    cur_sum -= arr[left]
    left += 1
    
  max_len += (right - left + 1)

print(max_len)
  