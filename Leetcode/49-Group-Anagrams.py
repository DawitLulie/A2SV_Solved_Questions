class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for word in strs:
            s = "".join(sorted(word))
            dic[s].append(word)

        return list(dic.values())



        
            



        