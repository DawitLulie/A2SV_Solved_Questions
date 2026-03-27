class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, cur_sum, path):
            if cur_sum >= n or len(path) == k:
                if len(path) == k and cur_sum == n:
                    result.append(path[:])
                return
            
            for i in range(start, 10):
                path.append(i)
                cur_sum += i

                backtrack(i+1, cur_sum, path)

                path.pop()
                cur_sum -= i
        
        backtrack(1, 0, [])

        return result

        