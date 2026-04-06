class Solution:
    def hIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2

            if nums[n - mid] >= mid:
                left = mid + 1

            else:
                right = mid - 1

        return right 
        