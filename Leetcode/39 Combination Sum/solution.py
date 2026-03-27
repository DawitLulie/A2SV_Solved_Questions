class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, cur_sum, path):
            if cur_sum >= target:
                if cur_sum == target:
                    result.append(path[:])
                return 

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                cur_sum += candidates[i]

                backtrack(i, cur_sum, path)

                path.pop()
                cur_sum -= candidates[i]

        backtrack(0, 0, [])

        return result
