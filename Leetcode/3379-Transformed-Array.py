class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)

        for i in range(len(nums)):
            index = (i + nums[i]) % n
            result.append(nums[index])
            
        return result

        