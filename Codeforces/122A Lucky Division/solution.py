n = int(input())

for i in range(4, n+1):
  if n % i == 0:
    s = str(i)

    if all(ch in "47" for ch in s):
      print("YES") 
      break

else:
  print("NO")
