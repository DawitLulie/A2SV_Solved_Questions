from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        dic = dict(sorted(dic.items(), key = lambda x: x[1]))
        result = []
        for key in dic:
                result.append(key)
        result.reverse()
        return result[:k]
      

      
       


    
        