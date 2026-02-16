from collections import Counter
class Solution:
    def isSubset(self, a, b):
        dic1 = Counter(a)
        dic2 = Counter(b)
        for key in dic2.keys():
            if dic2[key] > dic1[key]:
                return False
        return True
        