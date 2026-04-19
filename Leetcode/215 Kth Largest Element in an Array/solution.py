from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low = min(nums)
        high = max(nums)

        while low <= high:
            mid = low + (high - low) // 2

            count = 0
            for num in nums:
                if num >= mid:
                    count += 1
            
            if count < k:
                high = mid - 1
            else:
                low = mid + 1
                
        return high