from collections import Counter

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        counter = Counter()
        
        for key, val in nums1:
            counter[key] += val
            
        for key, val in nums2:
            counter[key] += val
            
        result = [[key, val] for key, val in counter.items()]
        result.sort()
        return result
