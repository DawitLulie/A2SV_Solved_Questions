class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        nums = [str(i) for i in range(1, n + 2)]
        self.result = ""
        used = [False] * (n + 1)

        def backtrack(s):
            if len(s) == n + 1:
                if not self.result or s < self.result:
                    self.result = s
                return
            
            for i in range(n + 1):
                if used[i]:
                    continue
                
                if len(s) > 0:
                    if pattern[len(s) - 1] == "I" and nums[i] < s[-1]:
                        continue
                    if pattern[len(s) - 1] == "D" and nums[i] > s[-1]:
                        continue
                
                used[i] = True
                backtrack(s + nums[i])
                used[i] = False

        backtrack("")
        return self.result