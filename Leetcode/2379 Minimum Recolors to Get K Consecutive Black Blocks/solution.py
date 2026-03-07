from collections import Counter
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        dic = Counter(blocks[:k])
        min_len = k - dic["B"]

        for i in range(k, len(blocks)):
            dic[blocks[i]] += 1
            num = blocks[i-k]
            dic[num] -= 1 
            if dic[num] == 0:
                del dic[num]
            min_len = min(min_len, k - dic["B"])

        return min_len
        