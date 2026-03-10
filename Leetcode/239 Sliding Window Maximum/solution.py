from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        for i in range(k):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)

        num = nums[stack[0]]
        result = [num]

        for i in range(k, len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            
            stack.append(i)

            while stack[0] <= i-k:
                stack.popleft()

            result.append(nums[stack[0]])
        
        return result

        
        
        