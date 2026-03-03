class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0:-1}
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]

            if k == 0:
                rem = prefix
            else:
                rem = prefix % k

            if rem in dic:
                if i - dic[rem] >= 2:
                   return True

            else:
               dic[rem] = i

        return False

        