from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic1 = Counter(chars)
        length = 0

        for word in words:
            dic2 = Counter(word)

            for key in dic2:
                if dic2[key] > dic1[key]:
                    break
            else:
                length += len(word)

        return length
            
        

            
        