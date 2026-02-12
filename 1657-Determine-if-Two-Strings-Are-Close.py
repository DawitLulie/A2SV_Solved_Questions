class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
            
        dic1 = Counter(word1)
        dic2 = Counter(word2)

        for key in dic1.keys():
            if key not in dic2:
                return False
        
        if sorted(dic1.values()) != sorted(dic2.values()):
            return False
        
        return True
