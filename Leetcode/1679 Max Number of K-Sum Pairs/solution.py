from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = Counter(nums)
        operations = 0

        for num in nums:
            x = k - num
            if x == num and dic[num] < 2:
                continue 

            if x in dic:
                operations += 1
                dic[x] -= 1

                if dic[x] == 0:
                     del dic[x]

                dic[num] -= 1
                if dic[num] == 0:
                    del dic[num]

        return operations
                