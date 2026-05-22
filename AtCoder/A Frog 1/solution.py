import sys

sys.setrecursionlimit(10**7)
n = int(input())
nums = list(map(int, input().split()))

memo = {}


def dp(i):
    if i >= n - 1:
        return 0

    if i not in memo:
        one = abs(nums[i] - nums[i + 1]) + dp(i + 1)
        two = float("inf")
        if i + 2 < n:
            two = abs(nums[i] - nums[i + 2]) + dp(i + 2)
        memo[i] = min(one, two)

    return memo[i]


print(dp(0))
