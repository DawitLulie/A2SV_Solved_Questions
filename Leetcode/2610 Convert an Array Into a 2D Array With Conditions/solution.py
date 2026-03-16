from collections import Counter
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = Counter(nums)
        matrix = []

        for i in range(len(nums)):
            seen = set()
            for num in nums:
                if dic[num] > 0 and num not in seen:
                    seen.add(num)
                    dic[num] -= 1

            if len(seen) == 0:
                break
            matrix.append(list(seen))
        
        return matrix
