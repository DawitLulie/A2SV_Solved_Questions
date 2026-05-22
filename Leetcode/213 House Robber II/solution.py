class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dp(i, n):
            if i >= n:
                return 0
            
            if (i, n) not in memo:
                memo[(i,n)] = max(dp(i+1,n), nums[i] + dp(i+2, n))
            
            return memo[(i,n)]
        
        return max(dp(0,n-1), dp(1, n))
        

        