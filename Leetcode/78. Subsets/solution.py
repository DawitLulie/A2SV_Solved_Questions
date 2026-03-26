class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, path: List[int]):
            # Add current subset to the result
            result.append(path[:])
            
            for i in range(start, len(nums)):
                # Include nums[i]
                path.append(nums[i])
                # Recurse
                backtrack(i + 1, path)
                # Backtrack
                path.pop()
        
        backtrack(0, [])
        return result
    