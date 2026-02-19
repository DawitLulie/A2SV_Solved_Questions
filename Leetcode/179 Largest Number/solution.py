class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        result =  "".join(sorted(nums, key = lambda x: x * 10, reverse = True))
        
        return "0" if result[0] == "0" else result

