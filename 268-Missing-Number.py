class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        myset  = set(nums)
        i, n = 0, len(nums)
        while i <= n:
            if i not in myset:
                return i
            i += 1
        
      
       

              