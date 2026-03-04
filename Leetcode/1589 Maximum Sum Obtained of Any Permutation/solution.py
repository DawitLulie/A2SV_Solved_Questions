class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0] * n

        for start, end in requests:
            prefix[start] += 1
            if end + 1 < n:
                prefix[end + 1] -= 1

        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        grid = sorted([(prefix[i], i) for i in range(n)], reverse=True)

        nums.sort(reverse=True)

        arr = [0] * n
        for i in range(n):
            arr[grid[i][1]] = nums[i]

        for i in range(1, n):
            arr[i] += arr[i - 1]

        result = 0
        for start, end in requests:
            if start == 0:
                result += arr[end]
            else:
                result += arr[end] - arr[start - 1]

        return result % (10**9 + 7)