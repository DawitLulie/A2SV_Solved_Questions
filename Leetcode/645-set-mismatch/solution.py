class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            index = nums[i] - 1

            if index != i and nums[index] != nums[i]:
                nums[index], nums[i] = nums[i], nums[index]

            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i+1]

        