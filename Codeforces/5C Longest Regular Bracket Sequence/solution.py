s = input()

stack = []
last = -1
max_len = 0
count = 0

for i in range(len(s)):
    if s[i] == ")":
        if not stack:
            last = i

        else:
            stack.pop()

            if stack:
                cur = i - stack[-1]
            else:
                cur = i - last

            if cur > max_len:
                max_len = cur
                count = 1
            elif cur == max_len:
                count += 1

    else:
        stack.append(i)


if max_len == 0:
    print(0,1)

else:
    print(max_len,count)