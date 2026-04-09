class Solution:
    def check(self, d, nums, m):
        count = 1
        last = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - last >= d:
                count += 1
                last = nums[i]

        return count >= m

    def maxDistance(self, nums: List[int], m: int) -> int:
        nums.sort()
        low = 1
        high = nums[-1] - nums[0]

        while low <= high:
            mid = (low + high) // 2

            if self.check(mid, nums, m):
                low = mid + 1
            else:
                high = mid - 1

        return high