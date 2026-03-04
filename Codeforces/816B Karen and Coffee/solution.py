n, k, q = map(int, input().split())
size  = 200002
prefix = [0] * size

for _ in range(n):
    l, r = map(int, input().split())
    prefix[l] += 1
    prefix[r + 1] -= 1

valid = [0] * size
for i in range(1, size):
    prefix[i] += prefix[i - 1]
    valid[i] = valid[i - 1] + (prefix[i] >= k)

for _ in range(q):
    l, r = map(int, input().split())
    print(valid[r] - valid[l - 1])