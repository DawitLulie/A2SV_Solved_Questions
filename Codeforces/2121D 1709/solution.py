t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    swap = []

    # sort arrays
    for i in range(n-1):
        changed = False
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap.append((1, j+1))
                changed = True

            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                swap.append((2, j+1))
                changed = True
        if not changed:
            break

    # fix cross condition
    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            swap.append((3, i+1))

    print(len(swap))
    for row in swap:
        print(*row)