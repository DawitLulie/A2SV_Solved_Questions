class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        cur = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            num = nums[i]
            if num < cur:
                cur = num
                continue

            if num % cur:
                l = num // cur
                cur = num // (l+1)
                operations += l

            else:
                operations += num // cur - 1

        return operations


           

        