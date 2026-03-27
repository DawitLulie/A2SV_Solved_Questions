class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()  # sort to handle duplicates
        result = []

        def backtrack(start, path):
            # add current subset
            result.append(path[:])

            for i in range(start, len(nums)):
                # skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # include nums[i]
                path.append(nums[i])

                # move forward
                backtrack(i + 1, path)

                # backtrack
                path.pop()

        backtrack(0, [])
        return result