from collections import Counter
class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return n

        nums.sort()
        dic = Counter(nums)
        count = 0

        for i in range(n):
            x = nums[i]

            if (n-i) - dic[x]  >= k:
                count += 1

            dic[x] -= 1

        return count 





