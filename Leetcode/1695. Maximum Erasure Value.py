class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        seen = set()
        left = 0
        current = 0
        answer = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                current -= nums[left]
                left += 1

            seen.add(nums[right])
            current += nums[right]
            answer = max(answer, current)

        return answer
