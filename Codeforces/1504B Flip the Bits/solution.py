from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(input())
    b = list(input())

    if a.count("1") != b.count("1"):
        print("NO")
        continue

    dic1 = Counter(a)
    dic2 = Counter(b)
    flip = 0

    for i in range(n-1, -1, -1):
        temp = a[i]
        if flip % 2 != 0:
            if temp == "1":
              temp = "0"
            else:
                temp = "1"

        if temp != b[i]:
            if dic1["1"] != dic1["0"]:
                print("NO")
                break

            flip += 1

        dic1[a[i]] -= 1
        if dic1[a[i]] == 0:
            del dic1[a[i]]

    else:
        print("YES")