class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s = ""
        for num in nums:
            s += str(num)
        result = []
        for ch in s:
            result.append(int(ch))
        return result
        