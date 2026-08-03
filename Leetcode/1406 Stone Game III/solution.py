class Solution:
    def stoneGameIII(self, nums: List[int]) -> str:
        n = len(nums)
        memo = {}

        def dp(i, turn):
            if i >= n:
                return 0
            
            if (i, turn) not in memo:
                if turn == 0:
                    res = float("-inf")
                    if i < n:
                        res = max(res, nums[i] + dp(i+1, 1-turn))
                    if i + 1 < n:
                        res = max(res, nums[i] + nums[i+1] + dp(i+2, 1-turn))
                    if i + 2 < n:
                        res = max(res, nums[i] + nums[i+1] + nums[i+2] + dp(i+3, 1-turn))
                    
                    memo[(i, turn)] = res
                    
                else:
                    res = float("inf")

                    if i < n:
                        res = min(res, dp(i+1, 1-turn))
                    if i + 1 < n:
                        res = min(res, dp(i+2, 1-turn))
                    if i + 2 < n:
                        res = min(res, dp(i+3, 1-turn))
                    
                    memo[(i, turn)] = res

            return memo[(i, turn)]
        
        res = dp(0, 0)
        total = sum(nums)


        if res > total / 2:
            return "Alice"

        elif res == total / 2:
            return "Tie"
        
        return "Bob"




        