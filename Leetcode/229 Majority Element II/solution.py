class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        arr = Counter(nums)
        n = len(nums)
        result = []
        for key, val in arr.items():
            if val > n / 3:
                result.append(key)
        return result

            

        