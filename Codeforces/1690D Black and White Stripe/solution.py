from collections import Counter
t = int(input())
for _ in range(t):
  n, k = list(map(int, input().split()))
  s = input()

  dic = Counter(s[:k])
  recolored = k - dic["B"]
  left = 0

  for right in range(k, n):
    dic[s[right]] += 1
    ch = s[left]
    dic[ch] -= 1

    if dic[ch] == 0:
      del dic[ch]
    left += 1

    recolored = min(recolored, k - dic["B"])

  print(recolored)

