from collections import Counter
class Solution:
    def checkEqual(self, a, b) -> bool:
        dic1 = Counter(a)
        dic2 = Counter(b)
        return dic1 == dic2
        
 