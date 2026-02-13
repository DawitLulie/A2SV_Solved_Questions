t = int(input())
for _ in range(t):
  n, x, k = list(map(int, input().split()))
  s = input()

  result = 0
  seconds = 0
  zero = False
  for i in range(min(n, k)):
    if s[i] == "L":
      x -= 1
    else:
      x += 1
  
    seconds += 1

    if x == 0:
      zero = True
      break

  if not zero:
    print(0)
    continue

  result += 1
  k -= seconds

  counts = {"L" : 0, "R" : 0}
  seconds = 0
  for i in range(min(n, k)):
    counts[s[i]] += 1
    seconds += 1

    if counts["L"] == counts["R"]:
      break

  if seconds > 0 and counts["L"] == counts["R"]:
    result += (k // seconds)

  print(result)