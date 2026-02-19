n, k = map(int, input().split())
arr = list(map(int, input().split()))

if k == 1:
    print(arr[-1] - arr[0])
else:
    gaps = []
    
    for i in range(1, n):
        gaps.append(arr[i] - arr[i - 1])
    
    gaps.sort(reverse=True)
    
    cost = arr[-1] - arr[0]
    
    for i in range(k - 1):
        cost -= gaps[i]
    
    print(cost)
