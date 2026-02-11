class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = Counter(nums)
        max_len = cur_len = 0
        for num in nums:
            if len(dic) == 0:
                return max_len

            if num not in dic or num - 1 in dic:
                continue
            
            while num in  dic:
                cur_len += 1
                del dic[num]
                num += 1
                
            max_len = max(max_len, cur_len)
            cur_len = 0

        return max_len
        