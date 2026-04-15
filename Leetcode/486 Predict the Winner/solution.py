from collections import defaultdict
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        visited = defaultdict(int)
        
        def dp(left, right, turn):
            if left > right:
                return 0
            
            if turn == 1:
                result = max(nums[left] + dp(left+1, right, 2),
                             nums[right] +  dp(left, right-1, 2))
            
            else:
                result = min(dp(left+1, right, 1), dp(left, right-1, 1))
            
            visited[(left, right, turn)] = result
            
            return result
        
        p1 = dp(0, len(nums)-1, 1)

        return sum(nums) - p1 <= p1
        