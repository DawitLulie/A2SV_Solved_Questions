from collections import Counter
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = Counter([0])
        prefix = 0
        subarrays = 0

        for num in nums:
            prefix += num
            rem = prefix - goal
            if rem in dic:
                subarrays += dic[rem]
        
            dic[prefix] += 1
        
        return subarrays
        




        
        