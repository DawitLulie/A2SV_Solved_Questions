class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}

        for i in range(len(list1)):
            dic[list1[i]] = i
        
        result = []
        min_index = float("inf")

        for i in range(len(list2)):
            s = list2[i]
            if s in dic:
                if min_index > i + dic[s]:
                    min_index = i + dic[s]
                    result = [s]

                elif min_index == i + dic[s]:
                    result.append(s)

        return result
                
            

