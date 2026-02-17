import math
n, m, a = list(map(int, input().split()))
flagstones = math.ceil(m / a) * math.ceil(n / a)
print(flagstones )