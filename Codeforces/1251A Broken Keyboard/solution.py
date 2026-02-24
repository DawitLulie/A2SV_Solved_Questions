t = int(input())
for _ in range(t):
  s = input()

  result = set()
  i = 0

  while i < len(s):
    cur = i
    while i < len(s) and s[i] == s[cur]:
      i += 1

    if (i - cur) % 2 != 0:
      result.add(s[cur])

  print("".join(sorted(result)))

