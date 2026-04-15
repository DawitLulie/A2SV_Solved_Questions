
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = set()
        i = 0
        
        while i < len(nums):
            index = nums[i] - 1
            
            if nums[i] != nums[index]:
                nums[index], nums[i] = nums[i], nums[index]
            else:
                if index != i and nums[i] not in result:
                    result.add(nums[i])
                i += 1

        return list(result)