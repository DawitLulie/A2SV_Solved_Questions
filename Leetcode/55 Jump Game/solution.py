class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
            
        cur = nums[0]
        for i in range(len(nums)):
            if cur == 0:
                return False
            cur = max(cur-1, nums[i])
        return True

        