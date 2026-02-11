class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        dic = Counter()
        result = ""
        for arr in responses:
            seen = set()
            
            for res in arr:
                if res not in seen:
                    seen.add(res)
                    dic[res] += 1

                    if not result:
                        result = res

                    elif dic[result] <= dic[res]:
                        if dic[result] < dic[res]:
                            result = res

                        if result > res:
                            result = res 

        return result
                    





        