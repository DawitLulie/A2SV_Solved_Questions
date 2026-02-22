class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)
        for i in range(min_, 0, -1):
             if max_ % i == 0 and min_ % i == 0:
                 return i