n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
day = 1

for i in range(n):
  if arr[i] >= day:
    result += 1
    day += 1
    
print(result)
