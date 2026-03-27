class Solution:
    def permute(self, nums):
        n = len(nums)
        result = []
        used = [False] * n

        def backtrack(path):
            if len(path) == n:
                result.append(path[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                
                path.append(nums[i])
                used[i] = True
                
                backtrack(path)
                
                path.pop()
                used[i] = False

        backtrack([])
        return result