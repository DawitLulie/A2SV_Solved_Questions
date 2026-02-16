class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dic1 = Counter(nums)
        dic2 = Counter()
        n = len(nums)

        for i in range(n):
            a = nums[i]
            dic2[a] += 1
            dic1[a] -= 1
            if dic1[a] == 0:
                del dic1[a]

            if dic2[a] > (i + 1) / 2 and dic1[a] > (n - i - 1) / 2:
                return i

        return -1
            
         
        
        