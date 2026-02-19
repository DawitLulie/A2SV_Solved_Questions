n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[n // 2]) if len(arr) % 2 != 0 else print(arr[n // 2 - 1])