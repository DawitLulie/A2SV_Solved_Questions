class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []  # To store all valid combinations
        candidates.sort()  # Sort to handle duplicates easily
        
        def backtrack(start, cur_sum, path):
            # If current sum reaches or exceeds target
            if cur_sum >= target:
                if cur_sum == target:  # If it's exactly target, save the combination
                    result.append(path[:])
                return  # Stop further exploration
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])  # Choose the candidate
                cur_sum += candidates[i]    # Update current sum

                backtrack(i+1, cur_sum, path)  # Recurse with next index

                path.pop()      # Backtrack: remove last candidate
                cur_sum -= candidates[i]  # Backtrack: revert sum

        backtrack(0, 0, [])  # Start backtracking from index 0

        return result  # Return all valid combinations