from sys import exit
from collections import defaultdict

n = int(input())
arr = [int(input()) for _ in range(n - 1)]

dic = defaultdict(list)
for i in range(n-1):
  index = i + 1

  dic[arr[i]].append(index+1)

for key, indices in dic.items():
  count = 0
  for index in indices:
    if index not in dic:
      count += 1

  if count < 3:
    print("No")
    exit()

print("Yes")

    
  
