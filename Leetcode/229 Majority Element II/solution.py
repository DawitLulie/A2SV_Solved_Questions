class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [num for num in counter if counter[num] > len(nums) // 3]
        

            

        