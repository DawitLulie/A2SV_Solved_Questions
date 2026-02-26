n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

i = j = 0
count = 0

while i < n and j < m:
    if arr1[i] < arr2[j]:
        i += 1
    elif arr1[i] > arr2[j]:
        j += 1
    else:
        cur = arr1[i]
        count1 = 0
        count2 = 0
        
        while i < n and arr1[i] == cur:
            count1 += 1
            i += 1
        
        while j < m and arr2[j] == cur:
            count2 += 1
            j += 1
        
        count += (count1 * count2)

print(count)