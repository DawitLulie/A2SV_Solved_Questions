from collections import Counter

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

dic = Counter()
left = 0
result = 0

for right in range(n):
  dic[arr[right]] += 1

  while len(dic) > k:
    key = arr[left]
    dic[key] -= 1

    if dic[key] == 0:
       del dic[key]
    left += 1
  
  result += (right - left + 1)

print(result)
  
    