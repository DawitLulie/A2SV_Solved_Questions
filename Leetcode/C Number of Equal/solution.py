from collections import Counter
n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
 
i = j = 0
count = 0
cur = prev = 0

while i < n and j < m:
  if i > 0 and arr1[i] == arr1[i-1]:
    count += prev
    i += 1
  
  elif arr1[i] == arr2[j]:
    cur += 1
    j += 1


  else:
    count += cur
    prev = cur
    cur = 0
    
    if arr1[i] > arr2[j]:
      j += 1
      
    else:
      i += 1

count += cur

print(count)

    
  
