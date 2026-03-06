from collections import Counter
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = Counter([0])
        prefix = 0
        subarrays = 0

        for i in range(len(nums)):
            prefix += nums[i]
            rem = prefix % k

            if rem in dic:
                subarrays += dic[rem]
            dic[rem] += 1

        return subarrays




        