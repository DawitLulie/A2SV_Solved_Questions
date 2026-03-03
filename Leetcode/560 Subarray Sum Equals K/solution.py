class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = Counter([0])
        subarrays = 0
        prefix = 0

        for num in nums:
            prefix += num
            if prefix - k in dic:
                subarrays += 1
            dic[prefix] += 1
            
        return subarrays
        