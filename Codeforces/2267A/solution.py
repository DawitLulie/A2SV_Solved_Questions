t = int(input())

for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()

    l, r = 0, n - 1

    count = 0
    while l < r:
        if s[l] != s[r]:
            if s[l] != c != s[r]:
                count += 2

            else:
                count += 1

        l += 1
        r -= 1

    print(count)
