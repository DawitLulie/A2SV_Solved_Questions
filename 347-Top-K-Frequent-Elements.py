class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        arr = dict(sorted(dic.items(), key = lambda x: x[1]))
        result = []
        count = 0
        for key in arr.keys():
                result.append(key)
        result.reverse()
        return result[:k]
      

      
       


    
        