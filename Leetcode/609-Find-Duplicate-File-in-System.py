class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for path in paths:
            root, *arr = path.split()
            for word in arr:
                key = val = ""
                condition = False
                for ch in word:
                    if ch == "(":
                        condition = True
                    if not condition:
                        val += ch
                    else:
                        key += ch

                val = root + "/" + val
                dic[key].append(val)
                
        result = []
        for arr in dic.values():
            if len(arr) > 1:
                result.append(arr)
        return result




        