from collections import Counter
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = Counter()
        stack = []
        

        for num in nums2:
            while stack and stack[-1] < num:
                dic[stack.pop()] = num

            stack.append(num)
        
        result = []
        for num in nums1:
            if num in dic:
                result.append(dic[num])
            
            else:
                result.append(-1)
                
        return result

        





        