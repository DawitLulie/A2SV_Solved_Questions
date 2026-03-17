from collections import Counter
from itertools import chain
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        minimum = min(min(basket1), min(basket2))

        dic1 = Counter(basket1)
        dic2 = Counter(basket2)
        arr1 = []
        arr2 = []

        for key in set(chain(dic1, dic2)):
            total = dic1[key] + dic2[key]
            if total % 2:
                return -1

            diff = abs(dic1[key] - dic2[key]) // 2

            if dic1[key] > dic2[key]:
                arr1.extend([key] * diff)
            elif dic2[key] > dic1[key]:
                arr2.extend([key] * diff)
        
        arr1.sort()
        arr2.sort(reverse=True)

        result = 0
        for i in range(len(arr1)):
            result += min(arr1[i], arr2[i], 2 * minimum)
        
        return result