from collections import Counter

t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    
    dic1 = Counter(arr[:l])
    dic2 = Counter(arr[l:])
    
    # Always make dic2 the bigger side
    if sum(dic1.values()) > sum(dic2.values()):
        dic1, dic2 = dic2, dic1
        
    # Remove already matched colors from both sides
    for key in list(dic1.keys()):
        m = min(dic1[key], dic2[key])
        dic1[key] -= m
        dic2[key] -= m
        
        if dic1[key] == 0:
            del dic1[key]
        if key in dic2 and dic2[key] == 0:
            del dic2[key]

    k = abs(r - l) // 2
    operation = k

    # Use pairs from bigger side to reduce balancing cost
    for key in list(dic2.keys()):
        if k == 0:
            break

        num = min(k, dic2[key] // 2)
        dic2[key] -= num * 2
        k -= num
        
        if dic2[key] == 0:
            del dic2[key]

    # Remaining unmatched socks need repaint operations
    operation += (sum(dic1.values()) + sum(dic2.values())) // 2

    print(operation)