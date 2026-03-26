s1 = input()
s2 = input()

target = s1.count('+') - s1.count('-')
count = 0
total = 0

def backtrack(index, cur):
    global count, total

    if index == len(s2):
        total += 1
        if cur == target:
            count += 1
        return

    if s2[index] == '+':
        backtrack(index + 1, cur + 1)

    elif s2[index] == '-':
        backtrack(index + 1, cur - 1)

    else:
        backtrack(index + 1, cur + 1)
        backtrack(index + 1, cur - 1)


backtrack(0, 0)

print(count / total)