class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        suffix = [nums[-1]]

        for i in range(1, n):
            prefix.append(nums[i] * prefix[-1])

        for i in range(n-2, -1, -1):
            suffix.append(nums[i] * suffix[-1])

        suffix.reverse()
        result = []

        for i in range(n):
            if i == 0:
                result.append(suffix[1])
                
            elif i == n - 1:
                result.append(prefix[i-1])

            else:
                result.append(prefix[i-1] * suffix[i+1])

        return result


     

        