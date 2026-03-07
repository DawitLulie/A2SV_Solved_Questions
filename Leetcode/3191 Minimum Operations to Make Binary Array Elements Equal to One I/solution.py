
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operation = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] = 1 - nums[i]
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]

                operation += 1
        return operation if sum(nums) == len(nums) else  -1
        