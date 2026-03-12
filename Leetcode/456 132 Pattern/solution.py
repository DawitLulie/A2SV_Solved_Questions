class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        

        third = []
        second = float("-inf")

        for i in range(len(nums)-1, -1, -1):
            if second > nums[i]:
                return True

            while third and third[-1] < nums[i]:
                second = third.pop()

            third.append(nums[i])


        return False

            
           
