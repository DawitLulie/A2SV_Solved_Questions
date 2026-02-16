class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        dic = Counter(changed)
        changed.sort()
        result = []
        
        for key in changed:
            if key in dic and key * 2 in dic:
                if key == key * 2 and dic[key] % 2 != 0:
                    return []

                result.append(key)
                dic[key] -= 1
                if dic[key] == 0:
                    del dic[key]

                dic[key * 2] -= 1
                if dic[key * 2] == 0:
                    del dic[key * 2]

    
            if len(result) == len(changed) / 2:
                return result

        return []
        
        