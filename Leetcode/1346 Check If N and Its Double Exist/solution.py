class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        return any(x * 2 in seen or x % 2 == 0 and x // 2 in seen or seen.add(x) for x in arr)
        