from collections import Counter
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dic = Counter()
        left = 0
        count = 0
        length = len(Counter(nums))

        for right in range(len(nums)):
            dic[nums[right]] += 1

            while len(dic) == length:
                count += len(nums) - right
                num = nums[left]
                dic[num] -= 1
                if dic[num] == 0:
                    del dic[num]
                left += 1

        return count
        