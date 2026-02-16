class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = Counter(magazine)
        for ch in ransomNote:
            if ch not in dic:
                return False

            dic[ch] -= 1
            if dic[ch] == 0:
                del dic[ch]
                
        return True
       
        