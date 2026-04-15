class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        nums = ["a", "b", "c"]
        result = []

        def backtrack(s):
            if len(result) == k:
                return
                
            if len(s) == n:
                result.append(s)
                return
            
            for i in range(3):
                if s and s[-1] == nums[i]:
                    continue

                backtrack(s + nums[i])

        backtrack("")
        
        if k > len(result):
            return ""
        
        return result[k-1]
        