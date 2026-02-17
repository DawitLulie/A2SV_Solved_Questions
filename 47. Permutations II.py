from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        arr = list(set(permutations(nums)))
        return arr
        