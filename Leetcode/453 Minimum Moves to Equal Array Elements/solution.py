class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[i] - nums[0] for i in range(1, len(nums)))

        