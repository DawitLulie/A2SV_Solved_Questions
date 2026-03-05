t = int(input())
for _ in range(t):
    n = int(input())
    red = list(map(int, input().split()))
    
    cur_sum = 0
    max1 = 0
    for num in red:
        cur_sum += num
        max1 = max(max1, cur_sum)
    
    m = int(input())
    blue = list(map(int, input().split()))
    
    cur_sum = 0
    max2 = 0
    for num in blue:
        cur_sum += num
        max2 = max(max2, cur_sum)
    
    print(max1 + max2)