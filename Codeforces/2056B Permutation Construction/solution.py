t = int(input())
for _ in range(t):
    n = int(input())

    p = []

    for i in range(n):
        nums = input()
        index = i

        for j in range(i):
            if nums[j] == "0":
                index -= 1

        p.insert(index, i + 1)

    print(*p)

