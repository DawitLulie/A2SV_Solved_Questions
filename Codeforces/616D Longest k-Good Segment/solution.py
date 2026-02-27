from collections import Counter

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
dic = Counter()

left = 0
max_len = 0
index = []

for right in range(n):
  dic[arr[right]] += 1
  while len(dic) > k:
    num = arr[left]
    dic[num] -= 1
    
    if dic[num] == 0:
       del dic[num]
    left += 1

  if max_len < right - left + 1:
    max_len = right - left + 1
    index = [left+1, right+1]

print(*index)
