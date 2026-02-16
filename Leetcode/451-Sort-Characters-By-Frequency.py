class Solution:
    def frequencySort(self, s: str) -> str:
        dic = Counter(s)
        arr = sorted(dic.items(), key = lambda x: x[1], reverse = True)
        result = []
        
        for key, val in arr:
            result.append(key * val)

        return "".join(result)






        