from collections import Counter
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        dic = Counter()
        max_len = 0
        left = 0

        for right in range(len(nums)):
            dic[nums[right]] += 1

            while dic[0] > 1:
                num = nums[left]
                dic[num] -= 1
                if dic[num] == 0:
                    del dic[num]
                left += 1

            max_len = max(max_len, right - left)

        return max_len

        