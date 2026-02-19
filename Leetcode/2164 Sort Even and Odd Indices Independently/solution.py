class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = deque(sorted([nums[i] for i in range(1, len(nums), 2)], reverse=True))
        even = deque(sorted([nums[i] for i in range(0, len(nums), 2)])) 

        result = []

        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even.popleft())  
            else:
                result.append(odd.popleft())   

        return result
