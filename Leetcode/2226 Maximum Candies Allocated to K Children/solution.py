class Solution:
    def check(self, candy, nums):
        cur = 0
        for num in nums:
            cur += num // candy
        return cur
            
    def maximumCandies(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 1   
        right = nums[-1]

        while left <= right:
            mid = (left + right) // 2

            if self.check(mid, nums) < k:
                right = mid - 1
            else:
                left = mid + 1
        
        return right