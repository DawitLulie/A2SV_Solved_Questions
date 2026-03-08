class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        prefix = [0] * (n+1)
        for l, r in queries:
            prefix[l] += 1
            prefix[r+1] -= 1
        
        for i in range(1, n+1):
            prefix[i] += prefix[i-1]
        
        for i in range(n):
            if nums[i] - prefix[i] > 0:
                return False
        
        return True
        