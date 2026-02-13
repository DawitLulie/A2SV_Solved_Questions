class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = defaultdict(list)
        pairs = 0
        
        for i, num in enumerate(nums):
            for j in dic[num]:
                if (i * j) % k == 0:
                    pairs += 1
                    
            dic[num].append(i)
        
        return pairs
        