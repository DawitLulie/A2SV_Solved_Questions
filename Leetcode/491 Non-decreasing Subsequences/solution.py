class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        result = []

        def backtrack(start, arr):
            if len(arr) > 1:
                result.append(arr[:])

            if start == n:
                return
            
            used = set()
            
            for i in range(start, n):
                if nums[i] in used:
                    continue
                
                if arr and arr[-1] > nums[i]:
                    continue
                
                arr.append(nums[i])
                used.add(nums[i])

                backtrack(i+1, arr)

                arr.pop()
        
        backtrack(0, [])

        return result